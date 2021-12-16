import itertools
import operator as op


def run_calculations(data):
    data = list(data)
    answers = {}
    answers["a"] = calc_a(data)
    answers["b"] = calc_b(data)
    return answers


def calc_a(x):
    """How many times does x increase?"""
    did_increase = where_increases(x)
    answer_a = sum(did_increase)
    return answer_a


def calc_b(x):
    """
    How many times does the rolling sum over
    3 values increase?
    """
    triplet_values = rolling_tuples(x, window_size=3)

    # Total value over the window
    triplet_totals = map(sum, triplet_values)

    # Frequency of increases
    did_increase = where_increases(triplet_totals)
    answer_b = sum(did_increase)

    return answer_b


def where_increases(x):
    paired_values = rolling_tuples(x, window_size=2)

    # Check if the current is less than next
    did_increase = itertools.starmap(op.lt, paired_values)

    return did_increase


def rolling_tuples(x, window_size=2):
    """
    Create iterable of tuples from rolling window over x
    starting from 0

    E.g.
    x = (a, b, c, d, e)
    n = 2 -> ((a, b), (b, c), (c, d))
    n = 3 -> ((a, b, c), (b, c, d))
    """
    x_offsets = itertools.tee(x, window_size)

    # Offset nth element by n indexes
    for i in range(1, window_size):
        for _ in range(i):
            # Offset by 1
            next(x_offsets[i])

    x_rolling = zip(*x_offsets)

    return x_rolling
