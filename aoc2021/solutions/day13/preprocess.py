import re
import itertools
from collections import defaultdict

X_MAX = 9999
Y_MAX = 9999


def preprocess(raw_data):
    points, folds = raw_data.split("\n\n")

    # Extract points at the start
    points = re.compile(r"(\d+),(\d+)(?=\n|$)").findall(points)
    points = itertools.starmap(lambda x, y: (int(x), int(y)), points)
    points = defaultdict(lambda: 0, dict(zip(points, itertools.repeat(1))))

    # Extract fold lines
    folds = re.compile(r"x=(\d+)|y=(\d+)").findall(folds)
    folds = itertools.starmap(
        lambda x, y: (int(x if x else X_MAX), int(y if y else Y_MAX)), folds
    )
    folds = list(folds)

    return points, folds
