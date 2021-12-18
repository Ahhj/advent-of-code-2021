import functools


def curried_split(sep=None):
    return functools.partial(str.split, sep=sep)


def preprocess(raw_data):
    data = raw_data.split("\n")
    data = map(curried_split(sep=" | "), data)
    signals, segments = zip(*data)
    signals = list(map(curried_split(sep=None), signals))
    segments = list(map(curried_split(sep=None), segments))
    return signals, segments
