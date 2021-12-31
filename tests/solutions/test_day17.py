import pytest

from aoc2021.solutions.day17.preprocess import preprocess
from aoc2021.solutions.day17.solve import *
from aoc2021.solutions.day17.target_area import TargetArea


@pytest.mark.parametrize(
    "raw_data, expected_result",
    [
        ("target area: x=20..30, y=-10..-5", TargetArea(20, 30, -10, -5)),
        ("target area: x=-20..-30, y=10..5", TargetArea(-20, -30, 10, 5)),
    ],
)
def test_preprocess(raw_data, expected_result):
    actual_result = preprocess(raw_data)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "probe, expected_hit",
    [
        (Probe(0, 0, 7, 2), True),
        (Probe(0, 0, 6, 3), True),
        (Probe(0, 0, 9, 0), True),
        (Probe(0, 0, 17, -4), False),
    ],
)
def test_step_to_target_area(probe, expected_hit):
    target_area = TargetArea(20, 30, -10, -5)
    hit = step_to_target_area(probe, target_area)
    assert hit == expected_hit


def test_solve_a():
    target_area = TargetArea(20, 30, -10, -5)
    actual_y_max = solve_a(target_area)
    expected_y_max = 45
    assert actual_y_max == expected_y_max


def test_solve_b():
    target_area = TargetArea(20, 30, -10, -5)
    actual_hits = solve_b(target_area)
    expected_hits = 112
    assert actual_hits == expected_hits
