def preprocess(raw_data):
    data = map(lambda s: s.split(" "), raw_data.split("\n"))
    return data
