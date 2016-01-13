import itertools
import re


def parse_input_str(input_str):
    tuples = []
    for line in input_str.split('\n'):
        pos_matches = re.match(
                r'([a-zA-Z]+) would gain ([0-9]+) happiness units by sitting next to ([a-zA-Z]+)', line)
        if pos_matches:
            tuples.append((pos_matches.group(1), pos_matches.group(3), int(pos_matches.group(2))))
        else:
            neg_matches = re.match(
                    r'([a-zA-Z]+) would lose ([0-9]+) happiness units by sitting next to ([a-zA-Z]+)', line)
            if neg_matches:
                tuples.append((neg_matches.group(1), neg_matches.group(3), -int(neg_matches.group(2))))

    return tuples


def get_cyclic_permutations_of_pairs(tuple):
    return filter(lambda (a, b): (tuple.index(b) - tuple.index(a)) in [1, -len(tuple) + 1],
                  list(itertools.permutations(tuple, 2)))


def add_a_guest(tuples, name):
    guests = set(map(lambda x: x[0], tuples))
    for guest in guests:
        tuples.append((guest, name, 0))
        tuples.append((name, guest, 0))


def get_non_cyclic_combinations_for_list(aList):
    all_combinations = list(itertools.permutations(aList, len(aList)))
    return set(all_combinations) - set(itertools.chain.from_iterable(
            map(lambda (j, comb): [comb[i:] + comb[:i] for i in range(j, len(comb))], enumerate(all_combinations))))


def get_optimal_arrangement_happiness_score(tuples):
    guests = set(map(lambda x: x[0], tuples))
    return \
        max(
            map(lambda option: sum(list(itertools.chain.from_iterable(
                map(lambda p:
                    map(lambda t: t[2],
                        filter(lambda x: (x[0] == p[0] and x[1] == p[1]) or (x[1] == p[0] and x[0] == p[1]), tuples)),
                            get_cyclic_permutations_of_pairs(option)
                    )
                )
            )), get_non_cyclic_combinations_for_list(guests)
            )
    )


tuples = parse_input_str('''Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George.''')

# Part 1
print get_optimal_arrangement_happiness_score(tuples)

# Part 2
add_a_guest(tuples, 'foo')
print get_optimal_arrangement_happiness_score(tuples)
