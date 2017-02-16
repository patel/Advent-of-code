def get_blocks_visited(dir_input):
    current_location = [0, 0]
    current_direction = 'U'
    for curr_dir_input in dir_input:
        direction, num_steps = curr_dir_input[0], curr_dir_input[1:]
        if current_direction == 'U':
            if direction == 'L':
                current_blocks_visited = map(lambda x: (current_location[0] - x, current_location[1]),
                                             range(1, int(num_steps) + 1))
                current_location[0] = current_location[0] - int(num_steps)
                current_direction = 'L'
            if direction == 'R':
                current_blocks_visited = map(lambda x: (current_location[0] + x, current_location[1]),
                                             range(1, int(num_steps) + 1))
                current_location[0] = current_location[0] + int(num_steps)
                current_direction = 'R'
        elif current_direction == 'D':
            if direction == 'L':
                current_blocks_visited = map(lambda x: (current_location[0] + x, current_location[1]),
                                             range(1, int(num_steps) + 1))
                current_location[0] = current_location[0] + int(num_steps)
                current_direction = 'R'
            if direction == 'R':
                current_blocks_visited = map(lambda x: (current_location[0] - x, current_location[1]),
                                             range(1, int(num_steps) + 1))
                current_location[0] = current_location[0] - int(num_steps)
                current_direction = 'L'

        elif current_direction == 'L':
            if direction == 'L':
                current_blocks_visited = map(lambda x: (current_location[0], current_location[1] - x),
                                             range(1, int(num_steps) + 1))
                current_location[1] = current_location[1] - int(num_steps)
                current_direction = 'D'
            if direction == 'R':
                current_blocks_visited = map(lambda x: (current_location[0], current_location[1] + x),
                                             range(1, int(num_steps) + 1))
                current_location[1] = current_location[1] + int(num_steps)
                current_direction = 'U'

        elif current_direction == 'R':
            if direction == 'L':
                current_blocks_visited = map(lambda x: (current_location[0], current_location[1] + x),
                                             range(1, int(num_steps) + 1))
                current_location[1] = current_location[1] + int(num_steps)
                current_direction = 'U'
            if direction == 'R':
                current_blocks_visited = map(lambda x: (current_location[0], current_location[1] - x),
                                             range(1, int(num_steps) + 1))
                current_location[1] = current_location[1] - int(num_steps)
                current_direction = 'D'
        yield current_blocks_visited


def solution_part_1(in_str):
    return _get_blocks_from_start(list(get_blocks_visited(in_str.split(', ')))[-1][-1])


def _get_blocks_from_start(location):
    return sum(map(abs, location))


def solution_part_2(in_str):
    visits = []
    for steps in get_blocks_visited(in_str.split(', ')):
        for step in steps:
            if step in visits:
                return _get_blocks_from_start(step)
            else:
                visits.append(step)


ip_str = open('input.txt', 'r').read()
print solution_part_1(ip_str)
print solution_part_2(ip_str)
