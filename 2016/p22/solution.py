import heapq
import itertools
import re
from collections import defaultdict
from pprint import pprint


class Node:
    def __init__(self, x, y, size, used, avail, p_used):
        self.x = x
        self.y = y
        self.id = "%s|%s" % (x, y)
        self.size = size
        self.used = used
        self.avail = avail
        self.p_used = p_used

    def __str__(self):
        return "%s/%s" % (self.x, self.y)

    def __repr__(self):
        return "%s/%s" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return int("%s%s" % (self.x, self.y))

    @classmethod
    def from_string(cls, ip_str):
        reg_search = re.search(
            r"\/dev\/grid\/node-x(?P<x>\w+)-y(?P<y>\w+)\s+(?P<size>\w+)T\s+(?P<used>\w+)T\s+(?P<avail>\w+)T\s+(?P<p_used>\w+)%",
            ip_str)
        if reg_search:
            return Node(int(reg_search.group('x')), int(reg_search.group('y')), int(reg_search.group('size')), \
                        int(reg_search.group('used')), int(reg_search.group('avail')), int(reg_search.group('used')))


def get_number_viable_pairs(ip_str):
    nodes = filter(lambda y: y, map(lambda x: Node.from_string(x), ip_str.split("\n")))
    return len(filter(lambda (a, b): (a.id != b.id and
                                      ((a.used > 0 and b.avail >= a.used) or (b.used > 0 and a.avail >= b.used))),
                      itertools.combinations(nodes, 2)))


def get_neighboring_nodes(node, nodes_by_index):
    possible_neighbors = filter(lambda (y, x): nodes_by_index.get(y) and nodes_by_index.get(y).get(x)
                                               and nodes_by_index.get(y).get(x) != '*',
                                [(node.y + 1, node.x), (node.y - 1, node.x), (node.y, node.x + 1),
                                 (node.y, node.x - 1)])
    return len(possible_neighbors) == len(filter(lambda (y, x): node.used <= nodes_by_index[y][x].size,
                                                 possible_neighbors))


def get_number_steps_with_astar(stateboard, nodes_by_index, init_node, target):
    heap = []
    heapq.heappush(heap, (0, (0, init_node)))

    visited = {init_node: 0}
    while heap:
        _, (num_steps, current_node) = heapq.heappop(heap)
        if current_node != target:
            next_steps = map(lambda (y, x): nodes_by_index[y][x],
                             filter(lambda (y, x): nodes_by_index.get(y) and nodes_by_index.get(y).get(x) and
                                                   stateboard[y][x] in ['.', '_'],
                                    [(current_node.y + 1, current_node.x), (current_node.y, current_node.x + 1),
                                     (current_node.y - 1, current_node.x), (current_node.y, current_node.x - 1)]))
            num_steps += 1
            for next_step in next_steps:
                if next_step in visited and num_steps >= visited[next_step]:
                    continue
                visited[next_step] = num_steps
                score = (target.y - next_step.y) ^ 2 + (target.x - next_step.x) ^ 2
                heapq.heappush(heap, (score, (num_steps, next_step)))
        else:
            return num_steps
    return -1


def get_stateboard(nodes_by_index):
    stateboard = defaultdict(dict)
    init_node = None
    for i in range(len(nodes_by_index)):
        for j in range(len(nodes_by_index.values()[i])):
            node = nodes_by_index[i][j]
            neighbors = get_neighboring_nodes(node, nodes_by_index)
            if node.used == 0:
                stateboard[node.y][node.x] = '_'
                init_node = node
            elif neighbors:
                stateboard[node.y][node.x] = '.'
            else:
                stateboard[node.y][node.x] = '*'
    return init_node, stateboard


def get_min_number_steps_to_last(ip_str):
    nodes_by_index = defaultdict(dict)

    nodes = filter(lambda y: y, map(lambda x: Node.from_string(x), ip_str.split("\n")))
    for node in nodes:
        nodes_by_index[node.y][node.x] = node

    init_node, stateboard = get_stateboard(nodes_by_index)

    if not init_node:
        return -1

    target = nodes_by_index[0][len(nodes_by_index[0]) - 2]
    total_steps = get_number_steps_with_astar(stateboard, nodes_by_index, init_node, target)

    # For swapping _ and the target node
    total_steps += 1

    init_node = nodes_by_index[0][len(nodes_by_index[0]) - 1]
    while stateboard[init_node.y][init_node.x - 1] == '.':
        if init_node.x in [1, 0] and init_node.y == 0:
            return total_steps
        stateboard[init_node.y][init_node.x - 1] = '*'
        target = nodes_by_index[init_node.y][init_node.x - 2]
        number_steps = get_number_steps_with_astar(stateboard, nodes_by_index, init_node, target)
        if number_steps == -1:
            break
        total_steps += (number_steps + 1)
        stateboard[init_node.y][init_node.x - 1] = '.'
        init_node = nodes_by_index[target.y][target.x + 1]
    return -1


ip_str = open('input.txt', 'r').read()

# a
print get_number_viable_pairs(ip_str)
# b
print get_min_number_steps_to_last(ip_str)
