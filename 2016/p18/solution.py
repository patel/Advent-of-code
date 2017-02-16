from collections import defaultdict


def get_next_list(input_list, num_cols):
    next_list = ['.'] * num_cols
    cnt = 0
    l, c, r = '.', input_list[0], input_list[1]
    for j in range(num_cols):
        if (l == '^' and r != '^' and (c == '^' or c != '^')) or \
                (l != '^' and r == '^' and (c != '^' or c == '^')):
            next_list[j] = '^'
        else:
            next_list[j] = '.'
            cnt += 1
        l = c
        c = r
        r = input_list[j + 2] if j < num_cols - 2 else '.'
    return next_list, cnt


def get_number_of_safe_tiles(input_list, max_row):
    i = 1
    current_total = len(filter(lambda y: '.' == y, input_list))
    num_cols = len(input_list)
    while True:
        if i >= max_row:
            break
        next_list, cnt = get_next_list(input_list, num_cols)
        current_total += cnt
        input_list = next_list
        i += 1
    return current_total


input_string = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
first_line_dict = list(input_string)

# i)
print get_number_of_safe_tiles(first_line_dict, 40)

# ii)
print get_number_of_safe_tiles(first_line_dict, 400000)
