import shortuuid
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from ..bot import dp
from ..models import UrlMapping


@dp.message(Command(commands=["baby"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(State("awaiting_url"))
    await message.reply("What is your target url?")


@dp.message(State("awaiting_url"))
async def good(message: types.Message, state: FSMContext):
    await state.clear()
    baby_url = shortuuid.uuid()
    await UrlMapping.objects.acreate(baby_url=baby_url, target_url=message.text)
    await message.reply(f"your baby url: {baby_url}")
