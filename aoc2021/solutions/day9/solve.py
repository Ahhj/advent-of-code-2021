import itertools
import functools
import operator as op
from collections import defaultdict

from ..day1.solve import rolling_tuples


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    """Find the total risk level across all the minima in the input grid"""
    minima_indexes = find_minima(data)
    minima_values = [data[i][j] for i, j in minima_indexes]
    answer_a = risk_level(minima_values)
    return answer_a


def solve_b(data):
    """Find the product of the sizes of the 3 largest connected components
    (aka basins)

    The connected components are centered on the minima of the input grid
    and expanded cell by cell (using 4-cell connectivity) until either the
    boundary of the grid is reached, or a cell has a value equal to the maximum
    value of the grid.
    """
    connected_components = find_connected_components(data)
    component_sizes = {k: len(v) + 1 for k, v in connected_components.items()}
    answer_b = functools.reduce(op.mul, sorted(component_sizes.values())[-3:])
    return answer_b


def risk_level(minima_values):
    """Calculate the risk level given minima for a grid"""
    return sum([v + 1 for v in minima_values])


def pad(x, value, nleft=1, nright=1):
    """Pad a value to the left and right of an interable"""
    lpad_values = itertools.repeat(value, times=nleft)
    rpad_values = itertools.repeat(value, times=nright)
    x_pad = itertools.chain(lpad_values, x, rpad_values)
    x_pad = tuple(x_pad)
    return x_pad


def find_minima(x):
    """Find the indexes of the minima in x"""
    indexed_row_col_minima = check_row_col_minima(x)

    # Filter where both row and column are minima
    indexed_mimina = filter(
        lambda item: op.and_(*item[1]), indexed_row_col_minima.items()
    )
    minima_indexes, _ = zip(*indexed_mimina)

    return minima_indexes


def check_row_col_minima(x):
    """Find cells of a grid that are minima in both the row and column directions"""
    x = list(x)
    row_minima = minima_along_axis(x, axis=0)
    col_minima = minima_along_axis(x, axis=1)
    col_minima = list(zip(*col_minima))

    # Assign indexes
    indexes = get_matrix_indexes(x)
    flat_row_minima = itertools.chain.from_iterable(row_minima)
    flat_col_minima = itertools.chain.from_iterable(col_minima)
    indexed_row_col_minima = zip(indexes, zip(flat_row_minima, flat_col_minima))
    return dict(indexed_row_col_minima)


def get_matrix_indexes(x):
    """Get a flat iterable of tuples, where each tuple gives the index of the
    corresponding element in the flattened input
    """
    nrows = len(x)
    ncols = len(x[0])
    indexes = itertools.product(range(nrows), range(ncols))
    return indexes


def minima_along_axis(x, axis=0):
    """Assign a boolean to each value in a grid to indicate whether the cells
    either side in a given direction have larger values that the cell in the center
    """
    x, x2 = itertools.tee(x)
    x_max = max(itertools.chain.from_iterable(x2))

    if axis == 1:
        # Transpose
        x = zip(*x)

    # Pad for boundaries
    x = map(functools.partial(pad, value=x_max), x)

    x_windows = map(functools.partial(rolling_tuples, window_size=3), x)
    x_windows = map(tuple, x_windows)
    is_minimum = functools.partial(itertools.starmap, lambda a, b, c: b < a and b < c)
    minima = map(is_minimum, x_windows)
    minima = map(tuple, minima)

    return minima


def find_connected_components(x):
    """Find the connected components (aka basins) of x"""
    x_flat = itertools.chain.from_iterable(x)
    x_flat, x_flat2 = itertools.tee(x_flat)

    # Build lookups: index to value map
    # Default to maximum value for boundary conditions
    # Cells with value < maximum will be included in a component
    x_max = max(x_flat)
    x_lookup = dict(zip(get_matrix_indexes(x), x_flat2))
    x_lookup = defaultdict(lambda: x_max, x_lookup)

    minima_indexes = find_minima(x)
    connected_components = defaultdict(lambda: [])

    # Consider cells to the left, right, up, down
    adjacent_differences = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i, j in minima_indexes:
        # Remove from lookups to avoid searching multiple times
        x_lookup.pop((i, j))
        edge_indexes = [(i, j)]  # Initially the edge is a single cell

        # Trace completion
        component_complete = False

        while not component_complete:
            new_edge_indexes = []

            for i2, j2 in edge_indexes:
                # Find the connected components of the edge cell
                for di, dj in adjacent_differences:
                    connected_index = (i2 + di, j2 + dj)

                    # Include if not boundary
                    if x_lookup[connected_index] < x_max:
                        # Remove from lookups to avoid searching multiple times
                        x_lookup.pop(connected_index)

                        # Update the connected component
                        connected_components[(i, j)].append(connected_index)

                        # Add the cell to the next set of edges to search
                        new_edge_indexes.append(connected_index)

            if new_edge_indexes:
                # Update the component edge for
                edge_indexes = new_edge_indexes[:]
            else:
                # No extra cells to search
                component_complete = True

    return connected_components
