def preprocess(raw_data):
    data = map(eval, raw_data.split("\n"))
    return list(data)
