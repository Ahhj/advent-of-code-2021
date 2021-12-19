import re


def preprocess(raw_data):
    polymer = tuple(raw_data.split("\n")[0])
    insertions = re.compile(r"([A-Z])([A-Z]) -> ([A-Z])").findall(raw_data)
    xs, ys, insertions = zip(*insertions)
    insertions = dict(zip(zip(xs, ys), insertions))
    return polymer, insertions
