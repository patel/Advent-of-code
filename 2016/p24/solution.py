import itertools
from collections import defaultdict


def is_connected_combination(pairs, target_pairs, part_b=False):
    reverse_lookup = {}
    lookup = {}
    for (x, y) in pairs:
        lookup[x] = y
        reverse_lookup[y] = x
    if part_b:
        if len(lookup) != target_pairs + 1 or len(reverse_lookup) != target_pairs + 1:
            return False
    nodes_visited = [False] * (target_pairs + 1)
    current_node = 0
    counter = target_pairs

    while counter >= 0:
        if current_node is not None:
            nodes_visited[current_node] = True
            next_node = lookup.pop(current_node, reverse_lookup.pop(current_node, None))
            if reverse_lookup.get(next_node) == current_node:
                del reverse_lookup[next_node]
            elif lookup.get(next_node) == current_node:
                del lookup[next_node]
            current_node = next_node
        counter -= 1
    return all(nodes_visited)


def get_pairs_cost_info(ip_str):
    graph = []
    numbers_lookup = []
    min_pairs = defaultdict(dict)
    cost_matrix = defaultdict(dict)
    i = 0

    for line in ip_str.split('\n'):
        current_list = list(line)
        numbers_lookup += [(int(n), (i, r)) for (r, n)
                           in filter(lambda (i, j): j not in ['#', '.'], enumerate(current_list))]
        graph.append(current_list)
        i += 1

    for num, num_location in numbers_lookup:
        locations = [num_location]
        distance = 0
        processed = []
        while locations:
            distance += 1
            neighbors = []
            for location in locations:
                neighbors += \
                    [(r, c) for (r, c) in [location[0] + 1, location[1]],
                                          [location[0] - 1, location[1]],
                                          [location[0], location[1] + 1],
                                          [location[0], location[1] - 1]
                     if 0 <= r < len(graph)
                     and 0 <= c < len(graph[r])
                     and (r, c) not in processed
                     and graph[r][c] != '#']
            neighbor_numbers = map(lambda x: int(graph[x[0]][x[1]]),
                                   filter(lambda x: graph[x[0]][x[1]] not in ['#', '.', str(num)], neighbors))
            for neighbor in neighbor_numbers:
                if not min_pairs.get(num) or not min_pairs[num].get(neighbor):
                    min_pairs[num][neighbor] = distance
                    cost_matrix[num][distance] = neighbor
            if len(min_pairs[num]) == len(numbers_lookup):
                break
            locations = [n for n in set(neighbors) if n not in processed]
            processed += neighbors
    return min_pairs, cost_matrix


def get_minimum_number_of_steps(min_pairs, cost_matrix, part_b=False):
    cost_neighbor_pairs = []
    for p0, p1 in cost_matrix.iteritems():
        cost_neighbor_pairs.append([(c, (p0, v)) for c, v in sorted(p1.iteritems())])

    options = cost_neighbor_pairs if part_b else cost_neighbor_pairs[:-1]

    min_count = None
    # Could improve the search space so that the first hit is minimum
    for option in itertools.product(*options):
        if is_connected_combination(map(lambda x: x[1], option), len(min_pairs) - 1, part_b):
            current_sum = sum(map(lambda x: x[0], option))
            if not min_count:
                min_count = current_sum
            else:
                min_count = min(current_sum, min_count)

    return min_count


def _solution():
    ip_str = open('input.txt', 'r').read()
    min_pairs, cost_matrix = get_pairs_cost_info(ip_str)
    print get_minimum_number_of_steps(min_pairs, cost_matrix)
    print get_minimum_number_of_steps(min_pairs, cost_matrix, part_b=True)


_solution()
