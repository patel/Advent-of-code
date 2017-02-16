import itertools


def find_number_valid_triangles(input_str):
    return len(filter(lambda (a, b, c): a + b > c,
                      map(lambda x: sorted(map(int, filter(lambda z: z != '', x.split('  ')))), input_str.split('\n'))))


def find_number_valid_triangles_vertically(x):
    columns = []
    for line in x.split('\n'):
        columns.append(map(int, filter(lambda z: z != '', line.split('  '))))
    transposed_columns = [list(x) for x in zip(*columns)]
    return sum(map(lambda t_column: len(filter(lambda (a, b, c): a + b > c,
                                               map(sorted, map(lambda x: t_column[x * 3:x * 3 + 3],
                                                               range(0, len(t_column) / 3))))), transposed_columns))


ip_str = open('input.txt', 'r').read()
# a
print find_number_valid_triangles(ip_str)
# b
print find_number_valid_triangles_vertically(ip_str)
