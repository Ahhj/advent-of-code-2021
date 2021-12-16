from dotenv import load_dotenv
from aocd import submit

from common.read_data import read_data
from common.download_data import download_data

load_dotenv()


class SolutionPipeline:
    def __init__(self, year, day, preprocess, run_calculations):
        self.year = year
        self.day = day
        self._preprocess = preprocess
        self._run_calculations = run_calculations
        self.raw_data = None
        self.answers = None

    def create(self):
        download_data(year=self.year, day=self.day)
        self.raw_data = read_data(year=self.year, day=self.day)

    def run(self):
        data = self._preprocess(self.raw_data)
        self.answers = self._run_calculations(data)

    def submit(self):
        submit(self.answers["a"], part="a", year=self.year, day=self.day)
        submit(self.answers["b"], part="b", year=self.year, day=self.day)
