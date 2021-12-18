def preprocess(raw_data):
    data = raw_data.split("\n\n")
    data = map(lambda x: map(lambda y: y.split(), x.split("\n")), data)

    (draw,) = next(data)
    draw = list(map(int, draw[0].split(",")))

    boards = [[[int(val) for val in row] for row in board] for board in data]

    return draw, boards
