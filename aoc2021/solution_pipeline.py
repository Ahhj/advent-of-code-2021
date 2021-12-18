import importlib
from dotenv import load_dotenv
from aocd import submit

from .read_data import read_data
from .download_data import download_data

load_dotenv()


class SolutionPipeline:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        solutions = importlib.import_module(f"aoc2021.solutions.day{day}")
        self._preprocess = solutions.preprocess
        self._solve = solutions.solve
        self.raw_data = None
        self.answers = None

    def create(self):
        download_data(year=self.year, day=self.day)
        self.raw_data = read_data(year=self.year, day=self.day)

    def run(self):
        data = self._preprocess(self.raw_data)
        self.answers = self._solve(data)

    def submit(self):
        submit(self.answers["a"], part="a", year=self.year, day=self.day)
        submit(self.answers["b"], part="b", year=self.year, day=self.day)
