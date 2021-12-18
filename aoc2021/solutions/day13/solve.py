from copy import deepcopy
from collections import defaultdict


def solve(data):
    points, folds = data
    answers = {}
    answers["a"] = solve_a(points, folds)
    answers["b"] = solve_b(points, folds)
    return answers


def solve_a(points, folds):
    points = deepcopy(points)

    for fold in folds:
        points = fold_along_axis(points, fold)
        break  # Only one fold

    answer_a = len(points)
    return answer_a


def solve_b(points, folds):
    points = deepcopy(points)

    for fold in folds:
        points = fold_along_axis(points, fold)

    print_projection(points)

    answer_b = input("Enter the code shown: ")
    return answer_b


def fold_along_axis(points, fold):
    new_points = defaultdict(lambda: 0)

    for (xp, yp), _ in points.items():
        point_ = get_folded_coords(xp, yp, *fold)
        new_points[point_] += 1

    return new_points


def get_folded_coords(xp, yp, xf, yf):
    xp_ = 2 * xf - xp if xp > xf else xp
    yp_ = 2 * yf - yp if yp > yf else yp
    return xp_, yp_


def print_projection(points):
    xs, ys = zip(*points.keys())
    ncols = max(xs) + 1
    nrows = max(ys) + 1
    grid = [["." for _ in range(ncols)] for _ in range(nrows)]
    for (x, y), _ in points.items():
        try:
            grid[y][x] = "#"
        except:
            print(x, y)
            raise

    print("\n".join(map("".join, grid)))
