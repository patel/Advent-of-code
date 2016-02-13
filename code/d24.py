from __future__ import print_function

import itertools

import numpy


def generate_combinations(opt_num_packages, package_weights, target_weight):
    return map(lambda t: (numpy.prod(t), t),
               filter(lambda x: sum(x) == target_weight,
                      itertools.combinations(package_weights, opt_num_packages)
                      )
               )


def calculate_min_quant_entanglement(package_weights, num_groups):
    package_weights.reverse()
    group_weight = sum(package_weights) / num_groups

    # Start at the minimum number of packages
    min_opt_num_packages = (group_weight / max(package_weights)) + 1

    for i in range(min_opt_num_packages, len(package_weights) + 1):
        combinations = generate_combinations(i, package_weights, group_weight)
        if combinations:
            return sorted(combinations, key=lambda x: x[0])[0][0]


package_weights = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                   107, 109, 113]
print(calculate_min_quant_entanglement(list(package_weights), 3))
print(calculate_min_quant_entanglement(list(package_weights), 4))
