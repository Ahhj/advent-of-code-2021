import functools


def preprocess(raw_data):
    data = raw_data.split("\n")
    data = map(tuple, data)
    data = map(functools.partial(map, int), data)
    data = list(map(tuple, data))
    return data
