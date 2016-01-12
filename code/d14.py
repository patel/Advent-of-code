import re


def get_distance_traveled(flying_speed, max_flying_time, resting_time, total_seconds):
    whole_intervals = total_seconds / (resting_time + max_flying_time)
    partial_interval_seconds = total_seconds % (resting_time + max_flying_time)
    return (partial_interval_seconds
            if partial_interval_seconds < max_flying_time
            else max_flying_time) * flying_speed + \
           whole_intervals * flying_speed * max_flying_time


def parse_input_str(input_str):
    reindeers = {}
    for line in input_str.split('\n'):
        matches = re.match(
                r'([a-zA-Z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.', line)
        reindeers[matches.group(1)] = (int(matches.group(2)), int(matches.group(3)), int(matches.group(4)))
    return reindeers


def get_max_from_list_of_reindeers(reindeers, num_seconds):
    return reduce(lambda x, y: max(x, y),
                  map(lambda v: get_distance_traveled(*(v + (num_seconds,))), reindeers.values()))


def get_max_score_from_list_of_reindeers(reindeers, num_seconds):
    scores_list = [0] * len(reindeers.keys())
    for i in range(1, num_seconds + 1):
        distance_traveled_list = map(lambda v: get_distance_traveled(*(v + (i,))), reindeers.values())
        winning_reindeers = [j for j, x in enumerate(distance_traveled_list) if x == max(distance_traveled_list)]
        for winning_reindeer in winning_reindeers:
            scores_list[winning_reindeer] = scores_list[winning_reindeer] + 1
    return max(scores_list)



reindeers = parse_input_str('''Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.''')


# Part 1
print get_max_from_list_of_reindeers(reindeers, 2503)

# Part 2
print get_max_score_from_list_of_reindeers(reindeers, 2503)
