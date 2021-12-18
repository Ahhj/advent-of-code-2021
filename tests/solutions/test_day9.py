import pytest

from aoc2021.solutions.day9.preprocess import preprocess
from aoc2021.solutions.day9.solve import solve_a, solve_b


EXAMPLE_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_solve_a(example_data):
    expected_value = 15
    actual_value = solve_a(example_data)
    assert expected_value == actual_value


def test_solve_b(example_data):
    expected_value = 1134
    actual_value = solve_b(example_data)
    assert expected_value == actual_value
