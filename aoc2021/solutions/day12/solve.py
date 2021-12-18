from collections import defaultdict
from copy import deepcopy


def solve(data):
    answers = {}
    answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(data):
    initial_node = "start"
    final_node = "end"
    links_initial = create_network(data)
    paths = distinct_paths(links_initial, initial_node, final_node)
    answer_a = len(paths)
    return answer_a


def solve_b(data):
    initial_node = "start"
    final_node = "end"
    links_initial = create_network(data)
    paths = distinct_paths_with_single_double_visit(
        links_initial, initial_node, final_node
    )
    answer_b = len(paths)
    return answer_b


def create_network(node_pairs):
    links = defaultdict(lambda: {"remaining_visits": 99999, "nodes": []})

    for x, y in node_pairs:
        links[x]["nodes"].append(y)
        links[y]["nodes"].append(x)

    for node in links:
        if node == node.lower():
            links[node]["remaining_visits"] = 1

    return links


def distinct_paths(
    links_initial,
    initial_node,
    final_node,
):
    links = deepcopy(links_initial)

    links[initial_node]["remaining_visits"] -= 1

    paths = []

    if initial_node == final_node:
        return [[final_node]]

    dest_nodes = links[initial_node]["nodes"]

    for node in dest_nodes:
        # Filter destination nodes that haven't been removed
        if links[node]["remaining_visits"] > 0:
            subpaths = distinct_paths(deepcopy(links), node, final_node)
            subpaths = [[initial_node, *path] for path in subpaths]
            paths += subpaths

    return paths


def distinct_paths_with_single_double_visit(links_initial, initial_node, final_node):
    paths = []

    for node in links_initial:
        if node == node.lower() and node not in (initial_node, final_node):
            links_copy = deepcopy(links_initial)
            links_copy[node]["remaining_visits"] = 2
            paths += distinct_paths(links_copy, initial_node, final_node)

    paths = list(set(map(tuple, paths)))
    return paths
