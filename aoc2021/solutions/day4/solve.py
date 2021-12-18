import itertools
import functools
import operator as op
from collections import defaultdict


def solve(data):
    data = list(data)
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    answer_a = get_score_by_board_rank(*data, 0)
    return answer_a


def solve_b(data):
    answer_b = get_score_by_board_rank(*data, -1)
    return answer_b


def get_score_by_board_rank(draw, boards, board_rank):
    board_bingo_indexes = get_board_bingo_indexes(draw, boards)
    sorted_indexes = sorted(board_bingo_indexes, key=lambda item: item[1])
    board_index, bingo_index = sorted_indexes[board_rank]
    return get_score(boards[board_index], draw, bingo_index)


def get_score(board, draw, bingo_index):
    all_drawn = draw[: bingo_index + 1]
    final_drawn = all_drawn[-1]
    flat_values = itertools.chain.from_iterable(board)
    remaining = filter(lambda x: x not in all_drawn, flat_values)
    return sum(remaining) * final_drawn


def get_board_bingo_indexes(draw, boards):
    nrows = len(boards[0])
    ncols = len(boards[0][0])

    # Track when each board reached bingo
    board_bingo_indexes = defaultdict(lambda: -1)

    for board_index, board in enumerate(boards):
        # Look up board square based on value
        flat_values = itertools.chain.from_iterable(board)
        flat_index = itertools.product(range(nrows), range(ncols))
        index_lookup = dict(zip(flat_values, flat_index))

        # Track how many of the row / column were checked
        row_counts = defaultdict(lambda: 0)
        col_counts = defaultdict(lambda: 0)

        for draw_index, drawn_val in enumerate(draw):
            i, j = index_lookup.get(drawn_val, (None, None))

            if i is not None:
                row_counts[i] += 1
                col_counts[j] += 1

                if row_counts[i] == nrows or col_counts[j] == ncols:
                    board_bingo_indexes[board_index] = draw_index
                    break

    # Remove boards that did hit bingo
    return filter(lambda item: item[1] != -1, board_bingo_indexes.items())
