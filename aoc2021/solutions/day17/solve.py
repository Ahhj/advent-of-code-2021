import itertools


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(target_area):
    def get_max_height(probe):
        # Check max height
        _, pys, _, _, _, _ = zip(*probe.history)
        return max(pys)

    y_max = 0
    vy_center = 0
    vx_min = 0
    vx_max = 100

    # Coarse grained search
    # Decrease the increment size each search
    for vy_inc in [100, 10, 1]:
        vy_range = 100 * vy_inc
        vy_min = vy_center - vy_range // 2
        vy_max = vy_center + vy_range // 2

        for vx0, vy0 in itertools.product(
            range(vx_min, vx_max), range(vy_min, vy_max, vy_inc)
        ):
            probe = Probe(0, 0, vx0, vy0)
            hit = step_to_target_area(probe, target_area)

            if hit:
                new_y_max = get_max_height(probe)
                if y_max < new_y_max:
                    y_max = new_y_max
                    vy_center = vy0
                    vx_min = vx0
                    vx_max = vx0 + 1

    return y_max


def solve_b(target_area):
    vx_min = 1
    vx_max = max(target_area.x1, target_area.x2) + 1
    vy_min = min(target_area.y1, target_area.y2)
    vy_max = 1000

    # Find minimum x and maximum y
    while vx_min < vx_max:
        for vy0 in reversed(range(vy_min, vy_max, 10)):
            probe = Probe(0, 0, vx_min, vy0)

            # On first hit, set a new maximum y
            if step_to_target_area(probe, target_area):
                vy_max = vy0
                break
        else:
            # If no maximum y found, increase minimum x
            vx_min += 1

        if vy_max < 1000:
            # Add increment size to include the true maximum
            vy_max += 10
            break

    hit_count = 0

    for vx0, vy0 in itertools.product(range(vx_min, vx_max), range(vy_min, vy_max)):
        probe = Probe(0, 0, vx0, vy0)
        hit_count += step_to_target_area(probe, target_area)

    return hit_count


def step_to_target_area(probe, target_area):
    x_lower = min(target_area.x1, target_area.x2)
    x_upper = max(target_area.x1, target_area.x2)
    y_lower = min(target_area.y1, target_area.y2)
    y_upper = max(target_area.y1, target_area.y2)

    while probe.px <= x_upper and probe.py >= y_lower:
        if x_lower <= probe.px <= x_upper and y_lower <= probe.py <= y_upper:
            return True

        probe.step()

    return False


class Probe:
    def __init__(self, px0, py0, vx0, vy0):
        self.px = px0
        self.py = py0
        self.vx = vx0
        self.vy = vy0
        self.history = []
        self.update_history()

    def step(self):
        self.update_position()
        self.update_velocity()
        self.update_history()

    def update_position(self):
        self.px += self.vx
        self.py += self.vy

    def update_velocity(self):
        self.vx += self.ax
        self.vy += self.ay

    def update_history(self):
        self.history.append((self.px, self.py, self.vx, self.vy, self.ax, self.ay))

    @property
    def ax(self):
        if self.vx:
            return -1
        else:
            return 0

    @property
    def ay(self):
        return -1
