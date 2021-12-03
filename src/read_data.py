import os
import pathlib
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))


def read_data(year, day):
    file_path = DATA_DIR / f"input_{year}_{day}.txt"

    with file_path.open("r") as f:
        data = f.read()

    return data
