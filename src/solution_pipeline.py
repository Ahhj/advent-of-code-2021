import itertools
from collections import OrderedDict

from src.read_data import read_data
from src.submit_answers import submit_answers
from src.download_data import download_data


class SolutionPipeline:
    def __init__(self, year, day, preprocess, calc_a, calc_b):
        self.year = year
        self.day = day
        self._preprocess = preprocess
        self._calc_a = calc_a
        self._calc_b = calc_b

    def create(self):
        download_data(year=self.year, day=self.day)

    def run(self):
        raw_data = read_data(year=self.year, day=self.day)
        data = self._preprocess(raw_data)
        answers = self._run_calculations(data)
        submit_answers(self.year, self.day, answers)

    def _run_calculations(self, data):
        # Copy consumables
        data_a, data_b = itertools.tee(data)

        # Answers need to be ordered!
        answers = OrderedDict()
        answers["a"] = self._calc_a(data_a)
        answers["b"] = self._calc_b(data_b)
        return answers
