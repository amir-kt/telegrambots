from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..bot import dp
from .strings import start_message


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await message.reply(start_message)
