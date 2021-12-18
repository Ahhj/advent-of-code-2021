import pytest
from aoc2021.solutions.day12.preprocess import preprocess
from aoc2021.solutions.day12.solve import solve_a, solve_b

EXAMPLE_DATA = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_solve_a(example_data):
    expected_result = 19
    actual_result = solve_a(example_data)
    assert expected_result == actual_result


def test_solve_b(example_data):
    expected_result = 103
    actual_result = solve_b(example_data)
    assert expected_result == actual_result
