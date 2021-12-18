import functools


def preprocess(raw_data):
    data = raw_data.split("\n")
    data = map(curried_split(" -> "), data)
    start_points, end_points = zip(*data)

    x1s, y1s = zip(*map(curried_split(","), start_points))
    x2s, y2s = zip(*map(curried_split(","), end_points))

    x1s = map(int, x1s)
    y1s = map(int, y1s)
    x2s = map(int, x2s)
    y2s = map(int, y2s)

    return zip(x1s, y1s, x2s, y2s)


def curried_split(sep=None):
    return functools.partial(str.split, sep=sep)
