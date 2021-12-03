import os
import pathlib
import datetime
from dotenv import load_dotenv
from aocd import get_data

load_dotenv()
DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))
START_YEAR = 2021


def download_data(year=None, day=None):
    data = get_data(year=year, day=day)

    file_path = DATA_DIR / f"input_{year}_{day}.txt"

    with file_path.open("w+") as f:
        f.write(data)


if __name__ == "__main__":
    current_dt = datetime.datetime.now()
    current_year = current_dt.year
    current_day = current_dt.day

    if current_dt.month != 12:
        # Advent hasn't started yet!
        current_year -= 1
        current_day = 25

    for year in range(START_YEAR, current_year + 1):
        for day in range(1, current_day + 1):
            download_data(year=year, day=day)
