import itertools
from collections import defaultdict
import itertools
from copy import deepcopy


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(risk_grid):
    path, risk = dijkstras_path(risk_grid)
    answer_a = risk
    return answer_a


def solve_b(risk_grid):
    nrows = len(risk_grid)
    ncols = len(risk_grid[0])
    risk_grid = tile_2d(risk_grid, 5, 5)

    for i, row in enumerate(risk_grid[:]):
        for j, _ in enumerate(row):
            # Offset by 1 for each row, col away from the original
            risk_grid[i][j] += i // nrows
            risk_grid[i][j] += j // ncols

            # Cycle
            risk_grid[i][j] -= 9 * ((risk_grid[i][j] - 1) // 9)

    path, risk = dijkstras_path(risk_grid)
    answer_b = risk
    return answer_b


def tile_2d(x, nrows, ncols):
    x_tiled = [
        list(itertools.chain(*[deepcopy(row) for _ in range(ncols)]))
        for _ in range(nrows)
        for row in x
    ]
    return x_tiled


def dijkstras_path(grid):
    """Use Dijkstras algorithm to find the path with the lowest cost

    See https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    nrows = len(grid)
    ncols = len(grid[0])

    initial_cell = (0, 0)
    target_cell = (nrows - 1, ncols - 1)

    coordinate_grid = get_coordinate_grid(nrows, ncols)

    all_cells = list(itertools.chain.from_iterable(coordinate_grid))
    visits_remaining = dict(zip(all_cells, itertools.repeat(1, len(all_cells))))
    prev_cells = {}
    distances = defaultdict(lambda: 9999, {initial_cell: 0})

    while any(visits_remaining.values()):
        remaining_distances = filter(
            lambda item: visits_remaining[item[0]] > 0, distances.items()
        )
        current_cell, _ = sorted(remaining_distances, key=lambda item: item[1])[0]
        visits_remaining[current_cell] -= 1

        if current_cell == target_cell:
            break

        i, j = current_cell
        neighbours = [
            (i - 1, j),  # Left
            (i + 1, j),  # Right
            (i, j - 1),  # Up
            (i, j + 1),  # Down
        ]

        neighbour_coords = [cell for cell in neighbours]

        for (i2, j2) in neighbour_coords:
            if visits_remaining.get((i2, j2), 0) > 0:
                current_distance = distances[(i2, j2)]
                possible_distance = distances[current_cell] + grid[i2][j2]
                if possible_distance < current_distance:
                    distances[(i2, j2)] = possible_distance
                    prev_cells[(i2, j2)] = current_cell

    path = []
    current_cell = target_cell
    if prev_cells.get(current_cell, False) or current_cell == initial_cell:
        while current_cell:
            path = [current_cell, *path]
            current_cell = prev_cells.get(current_cell, False)

    return path, distances[target_cell]


def get_coordinate_grid(nrows, ncols):
    coordinate_grid = itertools.product(range(nrows), range(ncols))
    coordinate_grid = itertools.tee(coordinate_grid, nrows)

    # Slices to get rows
    row_slices = zip(*pairwise(range(0, nrows * ncols + 1, ncols)))
    coordinate_grid = itertools.starmap(
        itertools.islice, zip(coordinate_grid, *row_slices)
    )
    coordinate_grid = map(list, coordinate_grid)
    coordinate_grid = list(coordinate_grid)

    return coordinate_grid


def pairwise(x):
    x1, x2 = itertools.tee(x)
    next(x2)
    return zip(x1, x2)
