import os
from time import sleep

from aiogram.types.input_file import FSInputFile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from .strings import fixture_pic_file_path


async def create_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/107.0.0.0 Safari/537.36"
    )
    chrome_options.page_load_strategy = "normal"

    return webdriver.Chrome(options=chrome_options)


async def scrape_game_info(team_name: str):
    driver = await create_chrome_driver()
    for round in range(1, 22):
        driver.get(
            "https://www.playhq.com/basketball-victoria/org/casey-basketball-association/senior-domestic-summer-202223"
            f"/thursday-men-b-grade/1035e459/R{round}"
        )
        sleep(1.5)

        # check to see if the first game's score is FINAL
        game_status = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/section/main/div/div/div[1]/section/section'
            "/div/div/div/div/ul/li/div[2]/div/div[1]/div[2]/span",
        ).text.lower()
        if game_status == "final":
            continue

        num_teams = len(
            driver.find_elements(
                By.XPATH,
                '//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div',
            )
        )

        for i in range(2, num_teams + 1):
            team1_name = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f"1]/div[1]/div/a ",
            ).text.lower()
            team2_name = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f"1]/div[3]/div/a ",
            ).text.lower()
            if team_name.lower() in [team1_name, team2_name]:
                datetime = driver.find_element(
                    By.XPATH,
                    f'//*[@id="root"]/section/main/div/div/div[1]/section'
                    f"/section/div/div/div/div/ul/li/div[{i}]/div/div["
                    f"2]/span[1]/div[2]/span ",
                ).text
                driver.close()
                return datetime.split(",")
    driver.close()


async def scrape_game_screenshot(team_name: str):
    driver = await create_chrome_driver()
    for round in range(1, 22):
        driver.get(
            "https://www.playhq.com/basketball-victoria/org/casey-basketball-association/senior-domestic-summer-202223"
            f"/thursday-men-b-grade/1035e459/R{round}"
        )
        sleep(1.5)

        # check to see if the first game's score is FINAL
        game_status = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/section/main/div/div/div[1]/section/section'
            "/div/div/div/div/ul/li/div[2]/div/div[1]/div[2]/span",
        ).text.lower()
        if game_status == "final":
            continue

        num_teams = len(
            driver.find_elements(
                By.XPATH,
                '//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div',
            )
        )

        for i in range(2, num_teams + 1):
            team1_name = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f"1]/div[1]/div/a ",
            ).text.lower()
            team2_name = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f"1]/div[3]/div/a ",
            ).text.lower()
            if team_name.lower() in [team1_name, team2_name]:
                required_width = driver.execute_script(
                    "return document.body.parentNode.scrollWidth"
                )
                required_height = driver.execute_script(
                    "return document.body.parentNode.scrollHeight"
                )
                driver.set_window_size(required_width, required_height)

                driver.find_element(
                    By.XPATH,
                    f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]',
                ).screenshot(fixture_pic_file_path(team_name))

                if os.path.exists(fixture_pic_file_path(team_name)):
                    return FSInputFile(fixture_pic_file_path(team_name))
    driver.close()
