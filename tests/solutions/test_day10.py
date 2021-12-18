import pytest
from aoc2021.solutions.day10.preprocess import preprocess
from aoc2021.solutions.day10.solve import solve_a, solve_b


EXAMPLE_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_solve_a(example_data):
    expected_result = 26397
    actual_result = solve_a(example_data)
    assert expected_result == actual_result


def test_solve_b(example_data):
    expected_result = 288957
    actual_result = solve_b(example_data)
    assert expected_result == actual_result
