import itertools
from .common import *


def preprocess(raw_data):
    data = map(lambda s: s.split(" "), raw_data.split("\n"))
    data = itertools.starmap(lambda d, m: Vector(Direction(d), int(m)), data)
    return data
