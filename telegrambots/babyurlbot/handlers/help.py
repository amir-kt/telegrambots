import strings
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..bot import dp


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await message.reply(strings.start_message)
