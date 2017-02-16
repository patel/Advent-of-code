import collections
import re


def sum_sector_ids_of_real_rooms(lines):
    sector_ids = 0
    for line in lines.split('\n'):
        m = re.match("([a-z\-]+)\-([0-9]+)\[([a-z]+)\]", line)
        encrypted_name, sector_id, checksum = m.group(1), m.group(2), m.group(3)
        if checksum == ''.join(map(lambda (x, y): x,
                                   sorted(collections.Counter(encrypted_name.replace("-", "")).most_common(),
                                          key=lambda x: (-x[1], ord(x[0])))))[0:5]:
            sector_ids += long(sector_id)
    return sector_ids


def get_decrypted_name_b(lines):
    def _decrypt(c, counter):
        if c == '-':
            return ' '
        return chr((ord(c) + counter - 97) % 26 + 97)

    for line in lines.split('\n'):
        m = re.match("([a-z\-]+)\-([0-9]+)", line)
        encrypted_name, sector_id = m.group(1), m.group(2)
        yield ''.join(map(lambda x: _decrypt(x, int(sector_id)), list(encrypted_name))), sector_id


def get_sector_id_for_matching_name(lines, target):
    for (decrypted_name, sector_id) in get_decrypted_name_b(lines):
        if decrypted_name == target:
            return sector_id

ip_str = open('input.txt', 'r').read()
# a
print sum_sector_ids_of_real_rooms(ip_str)
# b
print get_sector_id_for_matching_name(ip_str, 'northpole object storage')