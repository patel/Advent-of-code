import itertools
import re
from collections import defaultdict


def filter_key_from_ingredients(ingredients, key):
    if key is None:
        return
    for k, v in ingredients.iteritems():
        del v[key]


def generate_max_options(ingredients, max_val=100, filter_key='calories', filter_key_value=None, should_filter=False):
    filter_key_from_ingredients(ingredients, None)
    amount = 0
    all_options = generate_all_options(len(ingredients), max_val)
    transformed = get_transformed_ingredients(ingredients)
    filter_index = transformed.keys().index(filter_key)
    for option in all_options:
        comb = map(lambda x: sum(map(lambda t: int(t[0]) * int(t[1]), zip(x.values(), option))), transformed.values())
        if should_filter and comb[filter_index] == filter_key_value or not should_filter:
            amount = max(amount, reduce(lambda a, b: a * b if a > 0 and b > 0 else 0, comb) / comb[filter_index])
    return amount


def get_transformed_ingredients(ingredients):
    transformed = defaultdict(dict)
    for ingredient, value_objs in ingredients.iteritems():
        for k, v in value_objs.iteritems():
            transformed[k][ingredient] = v
    return transformed


def generate_all_options(dimensions, limit):
    args = []
    for i in range(0, dimensions):
        args.append(range(0, limit + 1))
    return filter(lambda x: sum(x) == limit, itertools.product(*args))


def read_ingredients(input_str):
    ingredients_lookup = {}
    for line in input_str.split('\n'):
        matches = re.match(r'([a-zA-Z]*): (.*)', line)
        ingredients_lookup[matches.group(1)] = {v[0]: int(v[1]) for v in
                                                map(lambda a: a.split(' '), matches.group(2).split(', '))}
    return ingredients_lookup


input_str = '''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'''

print generate_max_options(read_ingredients(input_str), 100, 'calories')
print generate_max_options(read_ingredients(input_str), 100, 'calories', 500, True)
