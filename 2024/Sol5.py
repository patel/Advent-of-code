import re

input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


def calcLowestLoc(input, is_part_two=False):
	lines = input.split('\n\n')
	seeds = map(int, lines[0].split('seeds: ')[1].split(' '))
	if is_part_two:
		seeds = map(int, lines[0].split('seeds: ')[1].split(' '))
	map_lookup = {}
	seed_locations = []
	keys_order = []
	for s_to_d_map in lines[1:]:
		map_lines = s_to_d_map.split('\n')
		match = re.search('(?P<source>.*)-to-(?P<destination>.*) map', map_lines[0])
		source, destination = match.group('source'), match.group('destination')
		map_lookup[(source, destination)] = []
		keys_order.append((source, destination))
		for map_line in map_lines[1:]:
			range_match = re.search('(?P<d_range>.*) (?P<s_range>.*) (?P<r_length>.*)', map_line)
			d_range, s_range, r_length = int(range_match.group('d_range')), int(range_match.group('s_range')), int(range_match.group('r_length'))
			map_lookup[(source, destination)].append((s_range, d_range, r_length))
	for seed in seeds:
		next_seed = seed
		locations = []
		for key in keys_order:
			for (s_r, d_r, r_l) in map_lookup[key]:
				if s_r <= next_seed < (s_r + r_l):
					next_seed = d_r + ( next_seed - s_r )
					break
		seed_locations.append(next_seed)
	return min(seed_locations)

print(calcLowestLoc(input))


