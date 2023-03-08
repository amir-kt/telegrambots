from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from ..bot import dp
from .utils import state_manager, strings
from .utils.scraper import scrape_game_info


class States(StatesGroup):
    selecting_team = State()
    team_selected = State()


@dp.message(Command(commands=["team"]))
async def team(message: types.Message, state: FSMContext):
    await state.set_state(States.selecting_team)
    await message.answer(strings.set_team_message)


@dp.message(States.selecting_team)
async def handle_team_name(message: types.Message, state: FSMContext):
    await state.set_state(States.team_selected)
    await state.set_data({"team_name": message.text})
    await message.answer(strings.team_selected(message.text))

    if await state_manager.set_game_info(await scrape_game_info(message.text), state):
        await state_manager.set_last_scrape_time(state)
