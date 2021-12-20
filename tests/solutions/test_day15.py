import pytest

from aoc2021.solutions.day15.preprocess import preprocess
from aoc2021.solutions.day15.solve import dijkstras_path, solve_a, solve_b, tile_2d

EXAMPLE_DATA = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_preprocess():
    actual_result = preprocess(EXAMPLE_DATA)
    expected_result = [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
    ]
    assert actual_result == expected_result


def test_dijkstras_path(example_data):
    basic_grid = [
        [1, 1, 1],
        [2, 2, 1],
        [1, 1, 1],
    ]
    actual_path, actual_action = dijkstras_path(basic_grid)
    expected_action = 4
    expected_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    assert actual_path == expected_path
    assert actual_action == expected_action

    basic_grid = [
        [1, 2, 1],
        [1, 2, 1],
        [1, 1, 1],
    ]
    actual_path, actual_action = dijkstras_path(basic_grid)
    expected_action = 4
    expected_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    assert actual_path == expected_path
    assert actual_action == expected_action

    basic_grid = [
        [1, 2, 1],
        [1, 1, 1],
        [2, 2, 1],
    ]
    actual_path, actual_action = dijkstras_path(basic_grid)
    expected_action = 4
    expected_path = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    assert actual_path == expected_path
    assert actual_action == expected_action

    larger_grid = [
        [1, 2, 2, 2, 2],
        [1, 1, 1, 2, 2],
        [2, 2, 1, 2, 2],
        [2, 2, 1, 2, 2],
        [2, 2, 1, 1, 1],
    ]
    actual_path, actual_action = dijkstras_path(larger_grid)
    expected_action = 8
    expected_path = [
        (0, 0),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (4, 3),
        (4, 4),
    ]
    assert actual_path == expected_path
    assert actual_action == expected_action

    actual_path, actual_action = dijkstras_path(example_data)
    expected_action = 40
    expected_path = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (2, 6),
        (3, 6),
        (3, 7),
        (4, 7),
        (5, 7),
        (5, 8),
        (6, 8),
        (7, 8),
        (8, 8),
        (8, 9),
        (9, 9),
    ]
    assert actual_path == expected_path
    assert actual_action == expected_action


def test_solve_b(example_data):
    expected_result = 315
    actual_result = solve_b(example_data)
    assert expected_result == actual_result


def test_tile_2d():
    x = [[1, 2], [3, 4]]
    actual_result = tile_2d(x, 2, 2)
    expected_result = [[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]]
    assert actual_result == expected_result
