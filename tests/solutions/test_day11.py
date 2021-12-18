import pytest
from aoc2021.solutions.day11.preprocess import preprocess
from aoc2021.solutions.day11.solve import solve_a, solve_b
from tests.solutions.test_day10 import EXAMPLE_DATA

EXAMPLE_DATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_solve_a(example_data):
    expected_result = 1656
    actual_result = solve_a(example_data)
    assert expected_result == actual_result


def test_solve_b(example_data):
    expected_result = 195
    actual_result = solve_b(example_data)
    assert expected_result == actual_result
