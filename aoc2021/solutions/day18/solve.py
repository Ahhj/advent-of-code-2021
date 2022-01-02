import itertools
import functools
from typing import Type


def solve(data):
    answers = {}
    # answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    result = snailfish_sum(data)
    return snailfish_magnitude(result)


def solve_b(data):
    # Pairwise sums
    pairs = itertools.permutations(data, 2)
    pairs = map(list, pairs)
    sums = map(solve_a, pairs)
    return max(sums)


def snailfish_add_reduce(x, y):
    """Apply snailfish addition and reduction"""
    result = [x, y]
    return snailfish_reduce(result)


def snailfish_reduce(x):
    """Reduce a snailfish number"""
    initial_x = None
    final_x = x[:]

    while final_x != initial_x:
        initial_x = final_x[:]
        final_x = snailfish_explode(initial_x)

        if final_x == initial_x:
            final_x = snailfish_split(final_x)
        else:
            continue

    return final_x


def snailfish_explode(x):
    """Explode the first 4-level nested pair"""
    x_indexed = assign_indexes(x)
    before_explode = itertools.takewhile(lambda elem: elem["level"] < 4, x_indexed)
    before_explode = list(before_explode)

    if len(before_explode) == len(x_indexed):
        # Nothing to explode
        return x[:]

    to_explode = x_indexed[len(before_explode) :][:2]
    replacement = {"level": 3, "value": 0}

    if len(before_explode) == 0:
        # Explode on the left-most edge
        after_explode = x_indexed[2:]
        right = {
            "level": after_explode[0]["level"],
            "value": after_explode[0]["value"] + to_explode[1]["value"],
        }
        x_exploded = [replacement, right, *after_explode[1:]]

    elif len(before_explode) + 2 < len(x_indexed):
        # Explode in the center
        after_explode = x_indexed[len(before_explode) :][2:]
        left = {
            "level": before_explode[-1]["level"],
            "value": before_explode[-1]["value"] + to_explode[0]["value"],
        }
        right = {
            "level": after_explode[0]["level"],
            "value": after_explode[0]["value"] + to_explode[1]["value"],
        }
        x_exploded = [
            *before_explode[:-1],
            left,
            replacement,
            right,
            *after_explode[1:],
        ]

    else:
        # Explode on the right-most edge
        left = {
            "level": before_explode[-1]["level"],
            "value": before_explode[-1]["value"] + to_explode[0]["value"],
        }
        x_exploded = [*before_explode[:-1], left, replacement]

    return remove_indexes(x_exploded)


def snailfish_sum(iterable):
    """Reduce the elements with snailfish addition"""
    return functools.reduce(snailfish_add_reduce, iterable)


def snailfish_split(x):
    """Split a snailfish number"""
    x_indexed = assign_indexes(x)

    before_split = itertools.takewhile(lambda elem: elem["value"] < 10, x_indexed)
    before_split = list(before_split)

    if before_split == x_indexed:
        # Nothing to split
        return remove_indexes(x_indexed)

    # Do the split
    to_split = x_indexed[len(before_split)]
    left = {"level": to_split["level"] + 1, "value": to_split["value"] // 2}
    right = {"level": to_split["level"] + 1, "value": (to_split["value"] + 1) // 2}
    after_split = x_indexed[len(before_split) + 1 :]

    # Create a new list from the split result
    x_split = [*before_split, left, right, *after_split]

    return remove_indexes(x_split)


def snailfish_magnitude(x):
    """Compute the magnitude of a snailfish number"""
    left, right = x
    result = 0

    if isinstance(left, int):
        result += 3 * left
    else:
        result += 3 * snailfish_magnitude(left)

    if isinstance(right, int):
        result += 2 * right
    else:
        result += 2 * snailfish_magnitude(right)

    return result


def assign_indexes(x):
    """Flatten a nested list and assign to each element label indicating the level in the original
    nested list.

    E.g. [1, [2]] --> [{'level': 0, 'value': 1}, {'level': 1, 'value': 2}]
    """
    x_indexed = []

    def traverse(y, level):
        if isinstance(y, int):
            return [{"level": level, "value": y}]
        else:
            return itertools.chain(*(traverse(elem, level + 1) for elem in y))

    x_indexed = list(itertools.chain(*(traverse(elem, 0) for elem in x)))

    return x_indexed


def remove_indexes(x_indexed):
    """Inverse operation of assign_indexes. Returns original nested list.

    Note: assumes pairwise structure of snailfish numbers"""

    max_levels = 4
    x = x_indexed[:]

    # Start from the lowest level
    for level in reversed(range(max_levels + 1)):
        new_x = []

        # Group the values at each level
        x_grouped = itertools.groupby(x, lambda d: d["level"])

        for group_level, group in x_grouped:
            # There are two options:
            #
            # 1. If the group_level is the lowest level (the one currently being iterated),
            # then the values in the group are split into pairs and each pair is
            # appended to new_a with the level + 1. I.e. the pair is nested
            # into the level above itself
            #
            # 2. Else, each member of the group is just appended to new_x

            if group_level == level:
                values = [g["value"] for g in group]

                if len(values) > 1:
                    for pair in distinct_pairwise(values):
                        new_x.append(
                            {
                                "level": level - 1,
                                "value": list(pair),
                            }
                        )
                else:
                    new_x.append({"level": level - 1, "value": values[:]})
            else:
                for g in group:
                    new_x.append(g)

        x = new_x[:]

    else:
        # Pluck the last remaining value
        x = x[0]["value"]

    return x


def pairwise(x):
    x1, x2 = itertools.tee(x)
    next(x2)
    return zip(x1, x2)


def distinct_pairwise(x):
    """Pairwise without overlaps between pairs"""
    pairs = pairwise(x)
    return itertools.islice(pairs, 0, len(x), 2)
