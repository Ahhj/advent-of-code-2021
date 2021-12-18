import re


def preprocess(raw_data):
    data = raw_data.split("\n")
    data = map(re.compile("-").split, data)
    data = list(data)
    return data
