from src.read_data import read_data
from src.submit_answers import submit_answers
from src.download_data import download_data

from solutions.day1.preprocess import preprocess
from solutions.day1.run_calculations import run_calculations

YEAR = 2021
DAY = 1

download_data(year=YEAR, day=DAY)
raw_data = read_data(year=YEAR, day=DAY)
data = preprocess(raw_data)
answers = run_calculations(data)
submit_answers(YEAR, DAY, answers)
