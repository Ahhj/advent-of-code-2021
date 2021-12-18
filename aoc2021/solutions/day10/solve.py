ALL_OPENS = ["(", "[", "<", "{"]
ALL_CLOSES = [")", "]", ">", "}"]

OPENS_CLOSES = dict(zip(ALL_OPENS, ALL_CLOSES))
CLOSES_OPENS = dict(zip(ALL_CLOSES, ALL_OPENS))


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(lines):
    score_lookup = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    errors = find_first_errors(lines)
    score = sum([score_lookup[actual] for i, expected, actual in errors.values()])
    return score


def solve_b(data):
    incomplete_lines = filter_incomplete_lines(data)
    n_incomplete_lines = len(incomplete_lines)
    answer_b = sorted(map(score_missing_closes, incomplete_lines))[
        n_incomplete_lines // 2
    ]
    return answer_b


def find_first_error(line):
    opens = []
    for character_index, character in enumerate(line):
        if opens:
            expected_close = OPENS_CLOSES.get(opens[-1])

        if character in ALL_OPENS:
            # Append open
            opens.append(character)
        elif character == expected_close:
            # Matching open and closed
            opens.pop(-1)  # Remove the open
        else:
            # Error!
            return (character_index, expected_close, character)

    return None


def find_first_errors(lines):
    errors = {}

    for line_index, line in enumerate(lines):
        e = find_first_error(line)
        if e is not None:
            errors[line_index] = e

    return errors


def filter_incomplete_lines(lines):
    errors = find_first_errors(lines)

    # Keep the incomplete lines
    line_indexes_with_errors = errors.keys()
    incomplete_lines = filter(
        lambda item: item[0] not in line_indexes_with_errors, enumerate(lines)
    )
    _, incomplete_lines = zip(*incomplete_lines)
    return incomplete_lines


def get_missing_closes(line):
    opens = []
    for character_index, character in enumerate(line):
        if opens:
            expected_close = OPENS_CLOSES.get(opens[-1])

        if character in ALL_OPENS:
            # Append open
            opens.append(character)
        elif character == expected_close:
            # Matching open and closed
            opens.pop(-1)  # Remove the open
        else:
            raise Exception("Line is invalid!")

    missing_closes = [OPENS_CLOSES[character] for character in opens]
    missing_closes = reversed(missing_closes)  # Close in reverse order

    return missing_closes


def score_missing_closes(line):
    score_lookup = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    missing_closes = get_missing_closes(line)

    # Get closes matching incomplete opens
    scores = [score_lookup[character] for character in missing_closes]
    total_score = 0
    for s in scores:
        total_score *= 5
        total_score += s

    return total_score
