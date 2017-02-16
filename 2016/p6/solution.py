from collections import Counter


def get_original_message(ip_str, part_b=False):
    return ''.join(map(lambda x: x[0][0], map(lambda x: sorted(x, key=lambda y: y[1] if part_b else -y[1])[0],
                                              [Counter(list(r)).items() for r in
                                               zip(*[list(ip_line) for ip_line in ip_str.split('\n')])])))


ip_str = open('input.txt', 'r').read()

# a
print get_original_message(ip_str)
# b
print get_original_message(ip_str, part_b=True)
