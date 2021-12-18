import itertools
from collections import OrderedDict


def solve(data):
    signals, segments = data
    answers = {}
    answers["a"] = solve_a(segments)
    answers["b"] = solve_b(signals, segments)
    return answers


def solve_a(segments):
    """Count numbers with unique lengths (1, 4, 7, 8)"""
    unique_length_number_map = {2: 1, 3: 7, 4: 4, 7: 8}
    unique_numbers_observed = []

    for s in segments:
        for block in s:
            number = unique_length_number_map.get(len(block))
            if number is not None:
                unique_numbers_observed.append(number)

    return len(unique_numbers_observed)


def solve_b(signals, segments):
    """Use the signals to decode the segments. Sum the resulting numbers."""
    decoded_numbers = list(itertools.starmap(decode, zip(signals, segments)))
    answer_b = sum(decoded_numbers)
    return answer_b


def decode(signals, segments):
    """Decode the segments given the signal and join the results to get the number
    that should've been shown on the output.

    This works by finding a vector which represent each number. The vector has
    the dimensions a-g, where 1 indicates that the letter appears in the signal
    that represents that number and a 0 indicates that it does not.

    For example, in the normal signal this looks like

      | a b c d e f g
    --|---------------
    0 | 1 1 1 0 1 1 1
    1 | 0 0 1 0 0 1 0
    2 | ...

    We can use known constrains on the vectors defining the rows and columns of
    the matrix above (such as the row/column sums), to find what the matrix looks
    like in the scrambled version. This can then be used to decode the segments
    in the outputs.

    """
    vector_number_mapping = get_number_vector_mapping(signals)
    segment_vectors = map(signal_to_vector, segments)
    decoded_segments = map(vector_number_mapping.get, segment_vectors)
    decoded_number = int("".join(map(str, decoded_segments)))
    return decoded_number


def get_number_vector_mapping(signals):
    """Find the vector that represents each number in the scrambled signals."""
    observed_vectors = get_initial_number_vector_mapping(signals)

    # Now need to use the unknown signals to get mappings between
    # numbers and signal vectors based on constraints between known
    # observations
    unknown_signals = [s for s in signals if len(s) in (5, 6)]

    # Need longest sequences first for conditions below (6 required to find 2/5)
    unknown_signals = reversed(sorted(unknown_signals, key=len))
    unknown_signals = list(unknown_signals)

    # Transpose to get mappings between numbers and vectors
    _, vectors = zip(*observed_vectors.items())
    vectors_t = list(zip(*vectors))

    for signal in unknown_signals:
        signal_vector = signal_to_vector(signal)
        contains1 = is_fully_contained(signal_vector, vectors_t[1])
        contains4 = is_fully_contained(signal_vector, vectors_t[4])
        contained_by_6 = is_fully_contained(vectors_t[6], signal_vector)

        if len(signal) == 6:
            if contains4:
                number = 9
            elif not contains1:
                number = 6
            else:
                number = 0
        elif contains1:
            number = 3
        elif contained_by_6:
            number = 5
        else:
            number = 2

        # Update observations
        vectors_t[number] = signal_vector

    # Mapping between vectors and numbers (used to look up signal vectors)
    vector_number_mapping = {
        tuple(vector): number for number, vector in enumerate(vectors_t)
    }

    return vector_number_mapping


def get_initial_number_vector_mapping(signal):
    # Only know unique length signals initially
    known_signals = {}
    signal_lengths = dict(zip(map(len, signal), signal))
    known_signals[1] = signal_lengths[2]
    known_signals[4] = signal_lengths[4]
    known_signals[7] = signal_lengths[3]
    known_signals[8] = signal_lengths[7]

    # Observed are unknown to start with
    letters = "abcdefg"
    observed_vectors = OrderedDict()
    for letter in letters:
        observed_vectors[letter] = [None] * 10

    # Update observed with initial observations
    for i, s in known_signals.items():
        for letter in letters:
            # Default to 0
            observed_vectors[letter][i] = 0

        for letter in s:
            observed_vectors[letter][i] = 1

    return observed_vectors


def signal_to_vector(signal):
    vector = OrderedDict()
    for letter in "abcdefg":
        vector[letter] = 1 if letter in signal else 0
    return tuple(vector.values())


def is_fully_contained(v1, v2):
    """Check if every element of v2 that is 1 is also 1 in v1
    i.e. that the number defined by v2 is fully contained withing
    v1. E.g. on a 7 segment display, all the segments in a 1 are
    also on when a 4 or a 7 is shown on the display.
    """
    for x, y in zip(v1, v2):
        if y == 1 and x == 0:
            return False
    else:
        return True
