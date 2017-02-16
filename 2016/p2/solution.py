def get_bathroom_code(code_map, code_lines):
    code_numbers = []
    prev_code_num = '5'

    for code_line in code_lines:
        for code in code_line:
            prev_code_num = code_map(prev_code_num, code)
        code_numbers.append(prev_code_num)
    return ''.join(code_numbers)


def code_map_1(code_num, code_char):
    return {
        '5': {
            'U': '3',
            'D': '8',
            'L': '4',
            'R': '6'
        },
        '1': {
            'U': '1',
            'D': '4',
            'L': '1',
            'R': '2'
        },
        '2': {
            'U': '2',
            'D': '5',
            'L': '1',
            'R': '3'
        },
        '3': {
            'U': '3',
            'D': '6',
            'L': '2',
            'R': '3'
        },
        '4': {
            'U': '1',
            'D': '7',
            'L': '4',
            'R': '5'
        },
        '6': {
            'U': '3',
            'D': '9',
            'L': '5',
            'R': '6'
        },
        '7': {
            'U': '4',
            'D': '7',
            'L': '7',
            'R': '8'
        },
        '8': {
            'U': '5',
            'D': '8',
            'L': '7',
            'R': '9'
        },
        '9': {
            'U': '6',
            'D': '9',
            'L': '8',
            'R': '9'
        }
    }[code_num][code_char]


def code_map_2(code_num, code_char):
    return {
        '5': {
            'U': '5',
            'D': '5',
            'L': '5',
            'R': '6'
        },
        '1': {
            'U': '1',
            'D': '3',
            'L': '1',
            'R': '1'
        },
        '2': {
            'U': '2',
            'D': '6',
            'L': '2',
            'R': '3'
        },
        '3': {
            'U': '1',
            'D': '7',
            'L': '2',
            'R': '4'
        },
        '4': {
            'U': '4',
            'D': '8',
            'L': '3',
            'R': '4'
        },
        '6': {
            'U': '2',
            'D': 'A',
            'L': '5',
            'R': '7'
        },
        '7': {
            'U': '3',
            'D': 'B',
            'L': '6',
            'R': '8'
        },
        '8': {
            'U': '4',
            'D': 'C',
            'L': '7',
            'R': '9'
        },
        '9': {
            'U': '9',
            'D': '9',
            'L': '8',
            'R': '9'
        },
        'A': {
            'U': '6',
            'D': 'A',
            'L': 'A',
            'R': 'B'
        },
        'B': {
            'U': '7',
            'D': 'D',
            'L': 'A',
            'R': 'C'
        },
        'C': {
            'U': '8',
            'D': 'C',
            'L': 'B',
            'R': 'C'
        },
        'D': {
            'U': 'B',
            'D': 'D',
            'L': 'D',
            'R': 'D'
        },
    }[code_num][code_char]


ip_str = open('input.txt', 'r').read()

# a
print get_bathroom_code(code_map_1, ip_str.split('\n'))
# b
print get_bathroom_code(code_map_2, ip_str.split('\n'))
