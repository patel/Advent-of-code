from __future__ import print_function
from __future__ import division
import numpy
import itertools
import math

def prime_generator():
    n = 2
    primes_set = set()
    while True:
        for prime in primes_set:
            if n % prime== 0:
                break
        else:
            primes_set.add(n)
            yield n
        n += 1

def get_first_prime_nums(n):
    i = 0
    primes = []
    for prime in prime_generator():
        primes.append(prime)
        i = i + 1
        if i == n:
            break
    return primes


def get_prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            factors.append(i)
            num = num / i
    if num > 1:
        factors.append(num)
    return factors

def get_all_factors(num):
    prime_factors = get_prime_factors(num)
    factors = set(prime_factors)
    i = 1
    while i <= len(prime_factors):
        reduce(lambda x, y: factors.add(numpy.prod(y)), itertools.combinations(prime_factors, i), [])
        i = i + 1
    factors.add(1)
    return factors

def get_all_factors_2(num):
    prime_factors = get_prime_factors(num)
    factors = set(prime_factors)
    i = 1
    while i <= len(prime_factors):
        for combination in itertools.combinations(prime_factors, i):
            prod = numpy.prod(combination)
            if prod * 50 > num:
                factors.add(prod)
        i = i + 1
    factors.add(1)
    return factors

def get_number_of_gifts(house_no, number_gifts_per_elf, factor_calculating_func):
    return sum(factor_calculating_func(house_no)) * number_gifts_per_elf

def generate_local_minima_primary_numbers_list(size):
    '''
    Generates the local minima which guarantees that number_gifts/house_number is the highest
    for the number of primary factors equal to `size`. In other words, no number lower than the generated value
    can have produce number of gifts.
    Background:
    Lowest number that generates the highest number of gifts, the pattern of sorted primary factors is following:
    [2,3]
    [2,2,3]
    [2,2,3,5]
    [2,2,2,3,5,7]
    [2,2,2,2,3,5,7]
    [2,2,2,2,3,5,7,11]
    :param size:
    :return:
    '''
    factors = []
    primary_nums = get_first_prime_nums(size)[1:]
    primary_nums.reverse()
    if size > 0:
        factors = list(itertools.repeat(2, int(size / 2)))
        i = size - len(factors)
        while i > 0:
            next_prime = primary_nums.pop()
            factors.append(next_prime)
            i = i - 1
    return factors


def get_minimum_house_number_with_target_gifts(target, number_gifts_per_elf, factor_calculating_func):
    '''
    Main handler
    :param target:
    :param number_gifts_per_elf:
    :param factor_calculating_func:
    :return:
    '''
    minima_list = None
    for i in range(2, int(numpy.log(target/10))):
        local_minima_list = generate_local_minima_primary_numbers_list(i)
        if get_number_of_gifts(numpy.prod(local_minima_list), number_gifts_per_elf, factor_calculating_func) < target:
            minima_list = local_minima_list
        else:
            break

    minima = numpy.prod(minima_list)
    incr = numpy.prod(minima_list[:int(len(minima_list) / 2)])
    i = minima

    while True:
        # Optimization: a number can only be considered if none of it's prime factors exceed the highest prime number of
        # the local minima
        if max(get_prime_factors(i)) > max(minima_list):
            i = i + incr
            continue
        if (get_number_of_gifts(i, number_gifts_per_elf, factor_calculating_func) > target):
            return i
        else:
            i = i + incr

# Part 1
print(get_minimum_house_number_with_target_gifts(33100000, 10, get_all_factors))

# Part 2
print(get_minimum_house_number_with_target_gifts(33100000, 11, get_all_factors_2))
