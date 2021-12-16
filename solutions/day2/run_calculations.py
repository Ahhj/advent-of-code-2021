from copy import deepcopy
import functools

from solutions.day2.common import Direction, Coordinates


def run_calculations(data):
    data = list(data)
    answers = {}
    answers["a"] = calc_a(data)
    answers["b"] = calc_b(data)
    return answers


def calc_a(vectors):
    initial_coords = Coordinates()
    final_coords = functools.reduce(update_position_a, vectors, initial_coords)
    answer_a = final_coords.depth * final_coords.horizontal
    return answer_a


def calc_b(vectors):
    initial_coords = Coordinates()
    final_coords = functools.reduce(update_position_b, vectors, initial_coords)
    answer_b = final_coords.depth * final_coords.horizontal
    return answer_b


def update_position_a(coords, vector):
    new_coords = deepcopy(coords)

    if vector.direction == Direction.forward:
        new_coords.horizontal += vector.magnitude
    else:
        # -1 if up, +1 if down
        multiplier = 1 - 2 * (vector.direction == Direction.up)
        depth_delta = multiplier * vector.magnitude
        new_coords.depth += depth_delta

    return new_coords


def update_position_b(coords, vector):
    new_coords = deepcopy(coords)

    if vector.direction == Direction.forward:
        new_coords.horizontal += vector.magnitude
        depth_delta = coords.aim * vector.magnitude
        new_coords.depth += depth_delta
    else:
        # -1 if up, +1 if down
        multiplier = 1 - 2 * (vector.direction == Direction.up)
        aim_delta = multiplier * vector.magnitude
        new_coords.aim += aim_delta

    return new_coords
