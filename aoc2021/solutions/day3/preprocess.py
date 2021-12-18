def preprocess(raw_data):
    data = raw_data.split("\n")
    data = map(tuple, data)
    data = map(lambda t: tuple(map(int, t)), data)
    return data
