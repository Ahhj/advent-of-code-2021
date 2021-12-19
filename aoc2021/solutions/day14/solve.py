import itertools
from copy import deepcopy
from collections import defaultdict


def solve(data):
    initial_polymer, insertions = data
    answers = {}
    answers["a"] = solve_a(initial_polymer, insertions)
    answers["b"] = solve_b(initial_polymer, insertions)
    return answers


def solve_a(initial_polymer, insertions):
    answer_a = solve_polymer_evolution(initial_polymer, insertions, 10)
    return answer_a


def solve_b(initial_polymer, insertions):
    answer_b = solve_polymer_evolution(initial_polymer, insertions, 40)
    return answer_b


def solve_polymer_evolution(initial_polymer, insertions, nsteps):
    """Evolve for a given number of steps and get the difference between the
    largest and smallest counts
    """
    polymer_pair_counts = evolve_polymer(initial_polymer, insertions, nsteps)

    base_counts = defaultdict(lambda: 0)
    for (x, y), pair_count in polymer_pair_counts.items():
        base_counts[x] += pair_count // 2
        base_counts[y] += pair_count // 2

    sorted_counts = sorted(base_counts.values())

    answer = sorted_counts[-1] - sorted_counts[0]

    return answer


def evolve_polymer(initial_polymer, insertions, nsteps):
    """Evolve the polymer by finding the counts of the new base pairs, without
    caring about ordering of the pairs within the polymer.

    The Solution just requires counts of each base, not the actual polymer
    which is computationally intensive to solve
    """

    polymer = deepcopy(initial_polymer)
    polymer_pair_counts = defaultdict(lambda: 0)
    for pair in pairwise(polymer):
        polymer_pair_counts[pair] += 1

    for _ in range(nsteps):
        new_polymer_pair_counts = defaultdict(lambda: 0)

        for (x, z), y in insertions.items():
            new_polymer_pair_counts[(x, y)] += polymer_pair_counts[(x, z)]
            new_polymer_pair_counts[(y, z)] += polymer_pair_counts[(x, z)]

        polymer_pair_counts = new_polymer_pair_counts

    return polymer_pair_counts


def pairwise(x):
    x1, x2 = itertools.tee(x, 2)
    next(x2)
    return zip(x1, x2)
