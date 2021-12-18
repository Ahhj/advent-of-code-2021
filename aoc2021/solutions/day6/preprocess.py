def preprocess(raw_data):
    data = raw_data.split(",")
    data = list(map(int, data))
    return data
