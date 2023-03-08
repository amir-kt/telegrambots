from aiogram import Bot

from .models import Schedule


async def send_reminders(bot: Bot):
    async for entry in Schedule.objects.all():
        await bot.send_message(
            chat_id=entry.chat_id,
            text=f"*{entry.team_name}*'s next game on *{entry.game_day},{entry.game_date}* is at *{entry.game_time}*",
            parse_mode="Markdown",
        )

    return "Ok"
