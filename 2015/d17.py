import itertools

def generate_combinations_to_target(containers, target):
    results = []
    for i in range(1, len(containers)):
         results = results + filter(lambda x: sum(x) == target, itertools.combinations(containers, i))
    return results


def get_total_number_combinations(containers, target):
    return len(generate_combinations_to_target(containers, target))


def get_total_min_number_cominations(containers, target):
    all_combinations = generate_combinations_to_target(containers, target)
    sorted(all_combinations, key=lambda x: len(x))
    min_combination = len(all_combinations[0])
    return len(list(itertools.takewhile(lambda x: len(x) == min_combination, all_combinations)))


# Part 1
print get_total_number_combinations([50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40], 150)

# Part 2
print get_total_min_number_cominations([50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40], 150)
