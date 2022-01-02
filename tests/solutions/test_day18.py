import pytest

from aoc2021.solutions.day18.preprocess import preprocess
from aoc2021.solutions.day18.solve import *


@pytest.mark.parametrize(
    "x, expected",
    [
        (
            [[[[[9, 8], 1], 2], 3], 4],
            [
                {"level": 4, "value": 9},
                {"level": 4, "value": 8},
                {"level": 3, "value": 1},
                {"level": 2, "value": 2},
                {"level": 1, "value": 3},
                {"level": 0, "value": 4},
            ],
        ),
        (
            [7, [6, [5, [4, [3, 2]]]]],
            [
                {"level": 0, "value": 7},
                {"level": 1, "value": 6},
                {"level": 2, "value": 5},
                {"level": 3, "value": 4},
                {"level": 4, "value": 3},
                {"level": 4, "value": 2},
            ],
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [
                {"level": 1, "value": 3},
                {"level": 2, "value": 2},
                {"level": 3, "value": 8},
                {"level": 3, "value": 0},
                {"level": 1, "value": 9},
                {"level": 2, "value": 5},
                {"level": 3, "value": 4},
                {"level": 4, "value": 3},
                {"level": 4, "value": 2},
            ],
        ),
    ],
)
def test_assign_indexes(x, expected):
    assert assign_indexes(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (
            [
                {"level": 4, "value": 9},
                {"level": 4, "value": 8},
                {"level": 3, "value": 1},
                {"level": 2, "value": 2},
                {"level": 1, "value": 3},
                {"level": 0, "value": 4},
            ],
            [[[[[9, 8], 1], 2], 3], 4],
        ),
        (
            [
                {"level": 0, "value": 7},
                {"level": 1, "value": 6},
                {"level": 2, "value": 5},
                {"level": 3, "value": 4},
                {"level": 4, "value": 3},
                {"level": 4, "value": 2},
            ],
            [7, [6, [5, [4, [3, 2]]]]],
        ),
        (
            [
                {"level": 1, "value": 3},
                {"level": 2, "value": 2},
                {"level": 3, "value": 8},
                {"level": 3, "value": 0},
                {"level": 1, "value": 9},
                {"level": 2, "value": 5},
                {"level": 3, "value": 4},
                {"level": 4, "value": 3},
                {"level": 4, "value": 2},
            ],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        ),
        (
            [
                {"level": 1, "value": 6},
                {"level": 2, "value": 5},
                {"level": 3, "value": 7},
                {"level": 3, "value": 0},
                {"level": 0, "value": 3},
            ],
            [[6, [5, [7, 0]]], 3],
        ),
        (
            [
                {"level": 3, "value": 0},
                {"level": 3, "value": 7},
                {"level": 2, "value": 4},
                {"level": 3, "value": 7},
                {"level": 3, "value": 8},
                {"level": 3, "value": 0},
                {"level": 3, "value": 13},
                {"level": 1, "value": 1},
                {"level": 1, "value": 1},
            ],
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
        ),
    ],
)
def test_remove_indexes(x, expected):
    assert remove_indexes(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (
            [[[[[9, 8], 1], 2], 3], 4],
            [[[[0, 9], 2], 3], 4],
        ),
        (
            [7, [6, [5, [4, [3, 2]]]]],
            [7, [6, [5, [7, 0]]]],
        ),
        ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
        (
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        ),
    ],
)
def test_snailfish_explode(x, expected):
    assert snailfish_explode(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ([10, 11], [[5, 5], 11]),
        ([11, 10], [[5, 6], 10]),
        (
            [[[[0, 7], 4], [15, [0, 13]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
        ),
    ],
)
def test_snailfish_split(x, expected):
    assert snailfish_split(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (
            [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
            [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]],
        ),
        (
            [
                [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
                [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
            ],
            [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],
        ),
    ],
)
def test_snailfish_reduce(x, expected):
    assert snailfish_reduce(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ([[1, 1], [2, 2], [3, 3], [4, 4]], [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]),
        (
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
            [[[[3, 0], [5, 3]], [4, 4]], [5, 5]],
        ),
        (
            [
                [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
                [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
                [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
                [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
                [7, [5, [[3, 8], [1, 4]]]],
                [[2, [2, 2]], [8, [8, 1]]],
                [2, 9],
                [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
                [[[5, [7, 4]], 7], 1],
                [[[[4, 2], 2], 6], [8, 7]],
            ],
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]],
        ),
    ],
)
def test_snailfish_sum(x, expected):
    assert snailfish_sum(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ([[1, 2], [[3, 4], 5]], 143),
        ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
        ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
        ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
        ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
        ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
        (
            [
                [[[6, 6], [7, 6]], [[7, 7], [7, 0]]],
                [[[7, 7], [7, 7]], [[7, 8], [9, 9]]],
            ],
            4140,
        ),
    ],
)
def test_snailfish_magnitude(x, expected):
    return snailfish_magnitude(x) == expected


def test_solve_a():
    example_data = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]],
    ]

    expected = 4140
    assert solve_a(example_data) == expected


def test_solve_b():
    example_data = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]],
    ]

    expected = 3993
    assert solve_b(example_data) == expected
