from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async

from ..bot import dp
from ..models import Schedule
from .utils import state_manager, strings
from .utils.scraper import scrape_game_info


class States(StatesGroup):
    setting_reminder_day = State()
    reminder_scheduled = State()


@dp.message(Command(commands=["reminder"]))
async def schedule_reminder(message: types.Message, state: FSMContext):
    team_name = await state_manager.get_team_name(state)
    if not team_name:
        await message.answer(strings.no_team_selected)
        return

    obj, _ = await Schedule.objects.aget_or_create(chat_id=message.chat.id)
    obj.team_name = team_name

    game_info = await scrape_game_info(team_name)
    if game_info:
        time, day, date = game_info
        obj.game_day = day
        obj.game_time = time
        obj.game_date = date

    await sync_to_async(obj.save)()

    keyboard_builder = InlineKeyboardBuilder()
    for day_choice in Schedule.Days:
        keyboard_builder.button(text=day_choice, callback_data=day_choice)
    keyboard_builder.adjust(2)

    await message.answer(
        "Please select which day you'd like to receive your reminder",
        reply_markup=keyboard_builder.as_markup(),
    )


@dp.callback_query()
async def schedule_reminder_call_back(callback_query: types.CallbackQuery):
    obj = await Schedule.objects.aget(chat_id=callback_query.message.chat.id)
    obj.reminder_day = callback_query.data
    await sync_to_async(obj.save)()

    await callback_query.message.edit_text(
        f"Your reminder for *{obj.team_name}* has been successfully scheduled for every *{obj.reminder_day}*",
        parse_mode="Markdown",
    )
