import itertools
from collections import Counter


def is_open_space(point, fav_number):
    (x, y) = point
    if x < 0 or y < 0:
        return False
    return Counter(bin(x * x + 3 * x + 2 * x * y + y + y * y + fav_number))['1'] % 2 == 0


def get_min_num_steps(start, target, fav_number):
    i = 0
    current_points = [start]
    while True:
        if target in current_points:
            return i
        current_points = list(set(filter(lambda (x, y): x >= 0 and y >= 0 and is_open_space((x, y), fav_number),
                                         list(itertools.chain(
                                             *map(lambda (x, y): [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)],
                                                  current_points))))))
        i += 1


def get_count_distinct_coordinates(start, num_steps, fav_number):
    i = 0
    current_points = [start]
    all_points = set(current_points)
    while True:
        if i == num_steps:
            return len(all_points)
        current_points = set(filter(lambda (x, y): x >= 0 and y >= 0 and is_open_space((x, y), fav_number),
                                    list(itertools.chain(
                                        *map(lambda (x, y): [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)],
                                             current_points)))))
        all_points.update(current_points)
        i += 1


# a
print get_min_num_steps((1, 1), (31, 39), 1364)
# b
print get_count_distinct_coordinates((1, 1), 50, 1364)