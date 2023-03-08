from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from ..bot import dp
from .utils import strings


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(State("started"))
    print(message)
    await message.answer(strings.start_message)
