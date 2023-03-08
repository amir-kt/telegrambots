import asyncio
import json

from aiogram.types import BotCommand
from asgiref.sync import async_to_sync
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .bot import dp, get_bot_instance
from .utils import send_reminders


def heartbeat(request):
    return HttpResponse("I'm OK.")


@csrf_exempt
@async_to_sync
async def bot_webhook(request, token):
    update = json.loads(request.body.decode("utf-8"))
    bot = await get_bot_instance(token)
    if not bot:
        return HttpResponse("Bot not registered.")

    await dp.feed_raw_update(bot, update)

    return HttpResponse("OK.")


@async_to_sync
async def setup_bot(request, token):
    if not settings.DEBUG:
        return HttpResponse("Not allowed.")

    bot = await get_bot_instance(token)
    if not bot:
        return HttpResponse("Bot not registered.")

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start the bot"),
            BotCommand(command="team", description="Choose your team name"),
            BotCommand(command="next", description="Displays the next game's details"),
            BotCommand(
                command="pic",
                description="Displays the next game's details as a picture",
            ),
            BotCommand(
                command="reminder",
                description="schedule a reminder to receive your game time every week",
            ),
        ]
    )
    return HttpResponse("OK.")


@async_to_sync
async def poll_bot_updates(request, token):
    if not settings.DEBUG:
        return HttpResponse("Not allowed.")

    bot = await get_bot_instance(token)
    if not bot:
        return HttpResponse("Bot not registered.")

    asyncio.create_task(dp.start_polling(bot))
    return HttpResponse("OK.")


@async_to_sync
async def send_fixtures(request, token):
    bot = await get_bot_instance(token)
    res = await send_reminders(bot)
    return HttpResponse(res)
