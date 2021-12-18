import itertools
import functools
from copy import deepcopy

from ..day9.solve import get_matrix_indexes


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    octopus_grid = get_initial_octopus_grid(data)
    n_flashed, octopus_grid = n_steps(octopus_grid, n=100)
    answer_a = sum(n_flashed)
    return answer_a


def solve_b(data):
    octopus_grid = get_initial_octopus_grid(data)
    first_step_index, _ = step_until_simultaneous_flash(octopus_grid)
    answer_b = first_step_index + 1
    return answer_b


def get_initial_octopus_grid(data):
    flat_data = itertools.chain.from_iterable(data)
    flat_indexes = get_matrix_indexes(data)
    octopus_grid = dict(zip(flat_indexes, map(Octopus, flat_data)))
    return octopus_grid


class Octopus:
    def __init__(self, initial_energy_level, flash_threshold=9):
        self.energy_level = initial_energy_level
        self.flash_threshold = flash_threshold
        self.flashed = False

    def add_energy_increment(self):
        self.energy_level += 1

    def reset(self):
        if not self.flashed:
            return
        else:
            self.flashed = False
            self.energy_level = 0

    def try_flash(self):
        if self.energy_level > self.flash_threshold:
            self.flashed = True


def flash(octopus_grid, i, j):
    octopus = octopus_grid.get((i, j), False)

    if not octopus:
        return
    elif octopus.flashed:
        return

    octopus.try_flash()

    if octopus.flashed:
        for di, dj in itertools.product(range(-1, 2), range(-1, 2)):
            neighbour_index = ((i + di), (j + dj))
            neighbour = octopus_grid.get(neighbour_index, False)

            if neighbour:
                neighbour.add_energy_increment()
                flash(octopus_grid, *neighbour_index)


def one_step(octopus_grid):
    stages = ["add_energy", "flash", "reset"]
    for stage in stages:
        for (i, j), octopus in octopus_grid.items():
            if stage == "add_energy":
                octopus.add_energy_increment()
            elif stage == "flash":
                flash(octopus_grid, i, j)
            elif stage == "reset":
                octopus.reset()

        if stage == "flash":
            octopi = octopus_grid.values()
            n_flashed = functools.reduce(
                lambda x, octopus: x + int(octopus.flashed), octopi, 0
            )

    return n_flashed


def n_steps(octopus_grid, n=1):
    octopus_grid = deepcopy(octopus_grid)
    n_flashed = []

    for i in range(n):
        n_flashed.append(one_step(octopus_grid))

    return n_flashed, octopus_grid


def step_until_simultaneous_flash(octopus_grid, max_iter=1000):
    octopus_grid = deepcopy(octopus_grid)

    for step_index in range(max_iter):
        n_flashed = one_step(octopus_grid)

        if n_flashed == len(octopus_grid):
            return step_index, octopus_grid
    else:
        return max_iter, octopus_grid
