import itertools


def get_next_potential_code(chars, min_chars_diff):
    i = len(chars) - 1
    wrapped = False
    while min_chars_diff > 0 or wrapped:
        if ord(chars[i]) == 122:
            chars[i] = 'a'
            i -= 1
            min_chars_diff -= 1
            wrapped = True
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            min_chars_diff -= 1
            wrapped = False


def get_next_password(chars):
    get_next_potential_code(chars, 1)
    while True:
        matching_conditions = int(len(set(chars).intersection({'i', 'o', 'l'})) == 0)
        positional_diff_by_one = map(lambda (a, b): str(ord(a) - ord(b)), zip(chars, chars[1:]))
        matching_conditions += '-1,-1' in (','.join(positional_diff_by_one))
        matching_conditions += positional_diff_by_one.count('0') >= 2 and \
                               len(set([chars[i] for i, val in enumerate(positional_diff_by_one) if val == '0'])) > 1
        if matching_conditions == 3:
            break
        else:
            get_next_potential_code(chars, 3 - matching_conditions)
    return chars


part_1 = get_next_password(list('vzbxkghb'))
part_2 = get_next_password(list(part_1))

print ''.join(part_1)
print ''.join(part_2)
