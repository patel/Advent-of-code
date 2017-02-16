import re


def get_disc_positions(ip_str):
    discs = {}
    for ip_line in ip_str.split('\n'):
        matches = re.search(
            r"Disc #(?P<disk>\w+) has (?P<num_pos>\w+) positions; at time=(?P<time>\w+), it is at position (?P<curr_pos>\w+).",
            ip_line)
        if matches:
            discs[int(matches.group('disk'))] = (
                int(matches.group('num_pos')), int(matches.group('time')), int(matches.group('curr_pos')))
    return discs


def get_lowest_time_for_button(discs):
    time_counter = 0
    while True:
        found = True
        for k, v in discs.iteritems():
            disc_num_pos, disc_init_time, disc_init_pos = v
            if (disc_init_pos + time_counter + k + disc_init_time) % disc_num_pos == 0:
                continue
            else:
                found = False
                break
        if found:
            return time_counter
        else:
            time_counter += 1


discs = get_disc_positions(open('input.txt', 'r').read())
# a
print get_lowest_time_for_button(discs)
discs[max(discs.keys()) + 1] = (11, 0, 0)
# b
print get_lowest_time_for_button(discs)
