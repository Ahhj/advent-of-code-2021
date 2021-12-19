import pytest
from aoc2021.solutions.day13.preprocess import preprocess
from aoc2021.solutions.day13.solve import solve_a  # , solve_b

EXAMPLE_DATA = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_solve_a(example_data):
    expected_result = 17
    actual_result = solve_a(*example_data)
    assert expected_result == actual_result
