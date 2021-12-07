import random
from collections import Counter


def calc_a(x_initial):
    x_initial = list(x_initial)
    x_align = find_alignment_position(x_initial, fuel_consumption_a)
    answer_a = fuel_consumption_a(x_initial, x_align)
    return answer_a


def calc_b(x_initial):
    x_initial = list(x_initial)
    x_align = find_alignment_position(x_initial, fuel_consumption_b)
    answer_b = fuel_consumption_b(x_initial, x_align)
    return answer_b


def fuel_consumption_a(x_initial, x_align):
    return sum(abs(x - x_align) for x in x_initial)


def fuel_consumption_b(x_initial, x_align):
    return sum(sum(range(1, abs(x - int(x_align)) + 1)) for x in x_initial)


def find_alignment_position(
    x_initial, fuel_consumption, delta_x=10, nsteps=1000, nretries=10, offset=100
):
    reversed_count = 0
    x_aligns = []

    for _ in range(nretries):
        # Start from mean
        x_align = sum(x_initial) / len(x_initial)
        # Offset by random number to avoid possible local minima
        x_align += random.randint(-1 * offset, offset)

        for t in range(1, nsteps + 1):
            new_x_align = x_align + delta_x
            current_fuel = fuel_consumption(x_initial, x_align)
            new_fuel = fuel_consumption(x_initial, new_x_align)

            if new_fuel > current_fuel:
                # Minimum in the opposite direction
                if reversed_count == 0:
                    # Reverse and keep delta the same
                    delta_x *= -1
                    reversed_count += 1
                elif reversed_count == 1:
                    # Minimum is between last point and current point
                    # Reverse again but reduce delta to 1
                    delta_x = 2 * (delta_x > 0) - 1
                    reversed_count += 1
                else:
                    break
            else:
                # Moving in the right direction!
                x_align = int(new_x_align)

        x_aligns.append(x_align)

    x_align = Counter(x_aligns).most_common()[0][0]

    return x_align
