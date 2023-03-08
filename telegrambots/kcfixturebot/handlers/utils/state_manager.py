import datetime

from aiogram.fsm.context import FSMContext


async def set_last_scrape_time(state: FSMContext):
    if state is not None:
        data = await state.get_data()
        data["last_scrape_time"] = datetime.datetime.utcnow()

        await state.set_data(data)


async def set_game_info(game_info: tuple[str, str, str], state: FSMContext):
    if game_info is not None and state is not None:
        data = await state.get_data()
        time, day, date = game_info

        data["game_date"] = date
        data["game_time"] = time
        data["game_day"] = day

        await set_last_scrape_time(state)

        await state.set_data(data)


async def get_team_name(state: FSMContext):
    data = await state.get_data()
    if data is not None and "team_name" in data:
        return data["team_name"]


async def get_game_date(state: FSMContext):
    data = await state.get_data()
    if data is not None and "game_date" in data:
        return data["game_date"]


async def get_game_time(state: FSMContext):
    data = await state.get_data()
    if data is not None and "game_time" in data:
        return data["game_time"]


async def get_last_scrape_time(state: FSMContext):
    data = await state.get_data()
    if data is not None and "last_scrape_time" in data:
        return data["last_scrape_time"]


async def is_game_info_expired(state: FSMContext):
    last_scrape_time = await get_last_scrape_time(state)
    if last_scrape_time:
        return datetime.datetime.utcnow() - last_scrape_time > datetime.timedelta(
            days=1
        )

    return False
