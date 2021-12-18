import pytest
import itertools
from aoc2021.solutions.day8.preprocess import preprocess
from aoc2021.solutions.day8.solve import solve_a, solve_b, decode

LARGER_EXAMPLE_DATA = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


@pytest.fixture()
def example_data():
    signals, segments = preprocess(LARGER_EXAMPLE_DATA)
    return signals, segments


def test_solve_a(example_data):
    expected_result = 26
    _, segments = example_data
    actual_result = solve_a(segments)
    assert expected_result == actual_result


def test_decode(example_data):
    expected_result = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    decoded_numbers = itertools.starmap(decode, zip(*example_data))
    assert list(decoded_numbers) == expected_result


def test_solve_b(example_data):
    expected_result = 61229
    actual_result = solve_b(*example_data)
    assert expected_result == actual_result
