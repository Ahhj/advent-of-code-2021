from collections import defaultdict


def calc_a(data):
    answer_a = population_after_ndays(data, 80)
    return answer_a


def calc_b(data):
    answer_b = population_after_ndays(data, 256)
    return answer_b


def population_after_ndays(initial_timers, ndays):
    timer_counts = defaultdict(lambda: 0)

    # Initial condition
    for timer in initial_timers:
        timer_counts[timer] += 1

    for _ in range(ndays):
        timer_counts = update_step(timer_counts)

    answer = sum(timer_counts.values())

    return answer


def update_step(timer_counts):
    # Simple transitions. Need to handle 0 and 7 specially due to spawn / merge.
    timer_transitions = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 8: 7}

    new_timer_counts = defaultdict(lambda: 0)
    new_timer_counts[6] = 0

    for timer, count in timer_counts.items():

        if timer != 0 and timer != 7:
            new_timer = timer_transitions[timer]
            new_timer_counts[new_timer] = count
        elif timer == 0:
            new_timer_counts[6] += count
            new_timer_counts[8] = count
        elif timer == 7:
            new_timer_counts[6] += count

    return new_timer_counts
