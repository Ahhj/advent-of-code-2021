import pytest
from collections import Counter
from aoc2021.solutions.day14.preprocess import preprocess
from aoc2021.solutions.day14.solve import (
    solve_polymer_evolution,
    evolve_polymer,
    pairwise,
)


EXAMPLE_DATA = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


@pytest.fixture()
def example_data():
    return preprocess(EXAMPLE_DATA)


def test_evolve_polymer(example_data):
    expected_polymer = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    counter = Counter(pairwise(expected_polymer))
    expected_result = dict(counter.items())

    initial_polymer, insertions = example_data
    actual_result = evolve_polymer(initial_polymer, insertions, 4)
    # Remove 0 counts for assertion
    actual_result = dict(filter(lambda item: item[1] > 0, actual_result.items()))
    assert expected_result == actual_result

    expected_length = len(expected_polymer)
    # Every base contributes 1 to the length (due to overlap), but final base contributes 2
    actual_length = sum(actual_result.values()) + 1
    assert expected_length == actual_length


def test_solve_polymer_evolution(example_data):
    nsteps = 10
    expected_result = 1588
    initial_polymer, insertions = example_data
    actual_result = solve_polymer_evolution(initial_polymer, insertions, nsteps)
    assert expected_result == actual_result

    nsteps = 40
    expected_result = 2188189693529
    initial_polymer, insertions = example_data
    actual_result = solve_polymer_evolution(initial_polymer, insertions, nsteps)
    assert expected_result == actual_result
