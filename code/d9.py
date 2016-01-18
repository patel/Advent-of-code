import itertools
import operator
import re
from collections import defaultdict, OrderedDict

import numpy


def covers_all_cities(total_paths, all_cities):
    cities_covered = [e for x in (map(lambda x: [x[0]] + [x[1]], total_paths)) for e in x]
    if len(total_paths) == (len(all_cities) - 1):
        for city in all_cities:
            if len(filter(lambda x: x == city, cities_covered)) > 2:
                return False
    else:
        return False
    return True


def get_shortest_path(inputs):
    distance_list, cities = inputs
    sorted_distance_list = sorted(distance_list, key=lambda x: x[2])
    last_index = 0
    total_paths = []
    for i, t in enumerate(sorted_distance_list):
        if len(filter(lambda x: x[1] == t[1] or x[0] == t[1], total_paths)) < 2 and \
                        len(filter(lambda x: x[1] == t[0] or x[0] == t[0], total_paths)) < 2:
            total_paths.append(t)
        last_index = i
        if covers_all_cities(total_paths, cities):
            break
    total_distance = sum(map(lambda x: x[2], total_paths))

    # Backtrack to find any min combinations
    for remaining_combo in itertools.combinations(sorted_distance_list[0:last_index + 1], len(cities) - 1):
        if (covers_all_cities(remaining_combo, cities)):
            total_distance = min(total_distance, sum(map(lambda x: x[2], remaining_combo)))
    return total_distance


def get_longest_path(inputs):
    distance_list, cities = inputs
    sorted_distance_list = sorted(distance_list, key=lambda x: -x[2])
    total_paths = []
    last_index = 0
    for i, t in enumerate(sorted_distance_list):
        if len(filter(lambda x: x[1] == t[1] or x[0] == t[1], total_paths)) < 2 and \
                        len(filter(lambda x: x[1] == t[0] or x[0] == t[0], total_paths)) < 2:
            total_paths.append(t)
        last_index = i
        if covers_all_cities(total_paths, cities):
            break

    total_distance = sum(map(lambda x: x[2], total_paths))

    # Backtrack to find any max combinations
    for remaining_combo in itertools.combinations(sorted_distance_list[0:last_index + 1], len(cities) - 1):
        if (covers_all_cities(remaining_combo, cities)):
            total_distance = max(total_distance, sum(map(lambda x: x[2], remaining_combo)))
    return total_distance


def parse_input_str(input_str):
    distance_list = []
    cities = set()
    for line in input_str.split('\n'):
        match_groups = re.match(r'([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)', line)
        distance_list.append((match_groups.group(1), match_groups.group(2), int(match_groups.group(3))))
        cities.add(match_groups.group(1))
        cities.add(match_groups.group(2))
    return (distance_list, cities)


input_str = '''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70'''

# Part 1
print get_shortest_path(parse_input_str(input_str))

# Part 2
print get_longest_path(parse_input_str(input_str))
