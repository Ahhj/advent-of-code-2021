import itertools
from collections import Counter


def solve(data):
    data = list(data)
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    # Transpose the data
    columns = zip(*data)

    # Get the most and least common values
    column_counters = map(Counter, columns)
    ordered_counts = map(Counter.most_common, column_counters)
    mc_vals, lc_vals = zip(*((mc[0], lc[0]) for mc, lc in ordered_counts))

    # Convert the binary numbers
    gamma_dec = binary_vector_to_int(mc_vals)
    epsilon_dec = binary_vector_to_int(lc_vals)

    answer_a = gamma_dec * epsilon_dec
    return answer_a


def solve_b(data):
    data_oxygen, data_co2 = itertools.tee(data)

    oxygen_bin = bit_criteria_filter(data_oxygen)
    oxygen_dec = binary_vector_to_int(oxygen_bin)

    co2_bin = bit_criteria_filter(data_co2, most_common=False)
    co2_dec = binary_vector_to_int(co2_bin)

    answer_b = oxygen_dec * co2_dec
    return answer_b


def binary_vector_to_int(x):
    x_bin = "".join(map(str, x))
    x_dec = int(x_bin, 2)
    return x_dec


def bit_criteria_filter(sequences, most_common=True):
    remaining = list(sequences)
    bit_index = 0

    while len(remaining) > 1:
        # Transpose the data
        columns = zip(*remaining)

        # Get the most / least common values in the relevant column
        selected_column = list(itertools.islice(columns, bit_index, bit_index + 1))[0]
        bit_counts = Counter(selected_column).most_common()
        mc_val, mc_count = bit_counts[0]
        lc_val, lc_count = bit_counts[-1]

        # Assign reference value for filtering
        if mc_count == lc_count:
            # Handle equally frequent values
            reference_value = int(most_common)
        elif most_common:
            reference_value = mc_val
        else:
            reference_value = lc_val

        # Filter bits based on equality with reference value
        remaining = filter(lambda seq: seq[bit_index] == reference_value, remaining)
        remaining = list(remaining)

        bit_index += 1

    return remaining[0]
