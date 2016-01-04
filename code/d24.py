from __future__ import print_function
import itertools
import numpy

package_weights = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
package_weights.reverse()
group_weight = sum(package_weights) / 3
print("Expected group weight %s" % group_weight)

def generate_combinations(opt_num_packages, package_weights, target_weight):
    return map(lambda t: (numpy.prod(t), t),
        filter(lambda x: sum(x) == target_weight,
          itertools.combinations(package_weights, opt_num_packages)
    )
)

# Start at the minimum number of packages
min_opt_num_packages = (group_weight / max(package_weights)) + 1
winning_combination = []

for i in range(min_opt_num_packages, len(package_weights)):
    combinations = generate_combinations(i, package_weights, group_weight)
    if combinations:
        sorted(combinations, key=lambda x: x[0])
        winning_combination = combinations[0]
        break

print(winning_combination[0])

""" Output:
Expected group weight 516
11266889531
"""