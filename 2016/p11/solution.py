import copy
import heapq
import itertools
import re
from collections import defaultdict
from pprint import pprint


class Component(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name and self.__class__ == other.__class__

    def __repr__(self):
        return self.__str__()


class Microchip(Component):
    def __init__(self, name):
        super(Microchip, self).__init__(name)

    def __str__(self):
        return "%s: %s" % ("Microchip", self.name)


class Generator(Component):
    def __init__(self, name):
        super(Generator, self).__init__(name)

    def __str__(self):
        return "%s: %s" % ("Generator", self.name)


def get_initial_setup(ip_str):
    floor_lookup_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    components = defaultdict(list)
    for ip_line in ip_str.splitlines():
        matches = re.search(r"The (?P<floor>\w+) floor contains (.+).", ip_line)
        floor, content = matches.group('floor'), matches.group(2)
        floor_index = floor_lookup_dict[floor]
        for and_components in content.split(' and '):
            for component in and_components.split(', '):
                generator_matches = re.search(r"a (?P<element>\w+) generator", component)
                if generator_matches:
                    components[floor_index].append(Generator(generator_matches.group('element')))
                microchip_matches = re.search(r"a (?P<element>\w+)\-compatible microchip", component)
                if microchip_matches:
                    components[floor_index].append(Microchip(microchip_matches.group('element')))
        components[4] = []
    return components


def get_min_steps(components, max_steps):
    heap = []
    heapq.heappush(heap, (0, (0, 1, components)))
    while True:
        if not heap:
            raise IndexError("Solution not possible")

        _, (num_steps, current_step, components) = heapq.heappop(heap)

        if all(map(lambda x: len(components[x]) == 0, range(1, max_steps))):
            return num_steps

        options = list(itertools.combinations(components[current_step], 2)) + \
                  list(itertools.combinations(components[current_step], 1))
        next_steps = [current_step + 1, current_step - 1]

        for next_step in next_steps:
            if next_step > max_steps or next_step < 1:
                continue
            for option in options:
                current_floor = [x for x in components[current_step] if x not in list(option)]
                next_floor = components[next_step] + list(option)
                prev_microchips = filter(lambda x: isinstance(x, Microchip), current_floor)
                prev_generators = filter(lambda x: isinstance(x, Generator), current_floor)
                next_microchips = filter(lambda x: isinstance(x, Microchip), next_floor)
                next_generators = filter(lambda x: isinstance(x, Generator), next_floor)

                for microchip in next_microchips:
                    if next_generators and \
                                    microchip.name not in map(lambda x: x.name, next_microchips):
                        continue
                for microchip in prev_microchips:
                    if prev_generators and \
                                    microchip.name not in map(lambda x: x.name, prev_microchips):
                        continue
                next_component = copy.deepcopy(components)
                next_component[current_step] = [x for x in next_component[current_step] if x not in list(option)]
                next_component[next_step] = next_component[next_step] + list(option)

                # Heuristic needs to be admissible (i.e. cost can't be greater than the actual cost)
                cost = -len(next_component[max_steps])
                heapq.heappush(heap, (cost, (num_steps + 1, next_step, next_component)))


ip_str = open('input.txt', 'r').read()
components = get_initial_setup(ip_str)

# a
print get_min_steps(components, 4)

components[1] = \
    components[1] + [Microchip('elerium'), Microchip('dilithium'), Generator('elerium'), Generator('dilithium')]

# b
print get_min_steps(components, 4)