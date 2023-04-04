from urllib.parse import urlparse

import shortuuid
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from asgiref.sync import sync_to_async

from ..bot import dp
from ..models import UrlMapping


@dp.message(Command(commands=["baby"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(State("awaiting_url"))
    await message.answer("What is your target url?")


@dp.message(State("awaiting_url"))
async def set_url(message: types.Message, state: FSMContext):
    await state.clear()
    target_url_parsed = urlparse(message.text)
    if not target_url_parsed.scheme:
        target_url_parsed = target_url_parsed._replace(scheme="https")
    target_url = target_url_parsed.geturl()

    baby_url = shortuuid.uuid()
    url_mapping = UrlMapping(baby_url=baby_url, target_url=target_url)
    await sync_to_async(url_mapping.save)()
    await message.answer(f"your baby url: https://babyurl.to/{baby_url}")
