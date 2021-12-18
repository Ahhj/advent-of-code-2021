import os
import pathlib
from dotenv import load_dotenv
from aocd import get_data

load_dotenv()
DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))


def download_data(year=None, day=None):
    data = get_data(year=year, day=day)

    file_path = DATA_DIR / f"input_{year}_{day}.txt"

    with file_path.open("w+") as f:
        f.write(data)
