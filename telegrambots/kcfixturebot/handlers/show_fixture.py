from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..bot import dp
from .utils import state_manager, strings
from .utils.scraper import scrape_game_info, scrape_game_screenshot


@dp.message(Command(commands=["next"]))
async def fixture_text(message: types.Message, state: FSMContext):
    try:
        team_name = await state_manager.get_team_name(state)
        if team_name is None:
            await message.answer(strings.no_team_selected)
            return

        # Only scrape the game data if necessary in order to save time
        if await state_manager.is_game_info_expired(state):
            game_info = await scrape_game_info(team_name)
            if game_info:
                await state_manager.set_game_info(game_info, state)

        await message.answer(
            strings.next_message(
                team_name,
                await state_manager.get_game_date(state),
                await state_manager.get_game_time(state),
            )
        )

    except RuntimeError:
        await message.answer(
            "Something went wrong! This could be because you've entered an invalid team name."
        )


@dp.message(Command(commands=["pic"]))
async def fixture_pic(message: types.Message, state: FSMContext):
    try:
        team_name = await state_manager.get_team_name(state)
        if team_name is None:
            await message.reply(strings.no_team_selected)
            return

        fixture_pic = await scrape_game_screenshot(team_name)
        if fixture_pic:
            # TODO: take the file_id and save it in database
            await message.reply_photo(fixture_pic)
        else:
            await message.reply("Couldn't retrieve picture")

    except RuntimeError:
        await message.reply(
            "Something went wrong! This could be because you've entered an invalid team name."
        )
