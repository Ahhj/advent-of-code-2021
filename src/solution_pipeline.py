from src.read_data import read_data
from src.submit_answers import submit_answers
from src.download_data import download_data


class SolutionPipeline:
    def __init__(self, year, day, preprocess, run_calculations):
        self.year = year
        self.day = day
        self._preprocess = preprocess
        self._run_calculations = run_calculations

    def create(self):
        download_data(year=self.year, day=self.day)

    def run(self):
        raw_data = read_data(year=self.year, day=self.day)
        data = self._preprocess(raw_data)
        answers = self._run_calculations(data)
        submit_answers(self.year, self.day, answers)
