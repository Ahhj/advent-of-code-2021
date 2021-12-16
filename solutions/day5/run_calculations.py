import itertools
from collections import defaultdict


def run_calculations(data):
    data = list(data)
    answers = {}
    answers["a"] = calc_a(data)
    answers["b"] = calc_b(data)
    return answers


def calc_a(endpoints):
    overlap_counts = count_line_overlaps(endpoints)
    answer_a = len(list(overlap_counts))
    return answer_a


def calc_b(endpoints):
    overlap_counts = count_line_overlaps(endpoints, include_diagonal=True)
    answer_b = len(list(overlap_counts))
    return answer_b


def points_along_line(x1, y1, x2, y2):
    if x1 == x2:
        npoints = abs(y2 - y1) + 1
        xs = itertools.repeat(x2, npoints)
    elif x1 < x2:
        xs = range(x1, x2 + 1)
    elif y1 > y2:
        xs = range(x2, x1 + 1)
    else:
        # Handle y1 < y2 but x2 < x1
        xs = reversed(range(x2, x1 + 1))

    if y1 == y2:
        npoints = abs(x2 - x1) + 1
        ys = itertools.repeat(y2, npoints)
    elif y1 < y2:
        ys = range(y1, y2 + 1)
    elif x1 > x2:
        ys = range(y2, y1 + 1)
    else:
        # Handle x1 < x2 but y2 < y1
        ys = reversed(range(y2, y1 + 1))

    return zip(xs, ys)


def count_line_overlaps(endpoints, include_diagonal=False):
    overlap_counts = defaultdict(lambda: 0)

    for x1, y1, x2, y2 in endpoints:
        if x1 == x2 or y1 == y2 or include_diagonal:
            line = points_along_line(x1, y1, x2, y2)

            for x, y in line:
                overlap_counts[(x, y)] += 1

    overlap_counts = filter(lambda item: item[1] > 1, overlap_counts.items())

    return overlap_counts
