import re


def preprocess(raw_data):
    pattern = re.compile(r"(\d+)(?=\n|$)")
    data = pattern.findall(raw_data)
    data = [[int(x) for x in row] for row in data]
    return data
