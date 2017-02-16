import re
from collections import defaultdict


def process_instructions(ip_str, h, w):
    out_matrix = [['.' for _ in range(h)] for _ in range(w)]
    for ip_line in ip_str.split('\n'):
        matches = re.search("rect (?P<mw>\w+)x(?P<mh>\w+)", ip_line)
        if matches:
            mw, mh = int(matches.group('mw')), int(matches.group('mh'))
            for i in range(mw):
                for j in range(mh):
                    out_matrix[i][j] = '#'
            continue
        matches = re.search("rotate column x=(?P<x>\w+) by (?P<y>\w+)", ip_line)
        if matches:
            y, x = int(matches.group("y")), int(matches.group("x"))
            out_matrix[x] = out_matrix[x][-y:] + out_matrix[x][:-y]
            continue

        matches = re.search("rotate row y=(?P<y>\w+) by (?P<x>\w+)", ip_line)
        if matches:
            x, y = int(matches.group("x")), int(matches.group("y"))
            column = [out_matrix[i][y] for i in range(w)]
            rotated_column = column[-x:] + column[:-x]
            for j in range(w):
                out_matrix[j][y] = rotated_column[j]
            continue
    return out_matrix


def print_matrix(m):
    z = zip(*m)
    for i in range(len(z)):
        print ' '.join([' ' if j == '.' else j for j in z[i]])
    print "\n"


def get_lit_pixels(ip_str, h, w, part_b=False):
    out_matrix = process_instructions(ip_str, h, w)
    if part_b:
        print_matrix(out_matrix)
    else:
        return len(filter(lambda x: x == '#', [item for sl in out_matrix for item in sl]))


# a
ip_str = open('input.txt', 'r').read()

# a
print get_lit_pixels(ip_str, 6, 50)
# b
get_lit_pixels(ip_str, 6, 50, part_b=True)
