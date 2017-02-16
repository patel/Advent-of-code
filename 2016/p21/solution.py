import re


def swap_position(s, x, y):
    tmp = s[x]
    s[x] = s[y]
    s[y] = tmp


def move_postion(s, x, y):
    popped_element = s.pop(y)
    return s[:x] + [popped_element] + s[x:]


def parse_instructions(ip_lines):
    formatted_instructions = []
    regular_expressions = {
        'swap position': 'swap position (?P<x>\w+) with position (?P<y>\w+)',
        'swap letter': 'swap letter (?P<x>\w+) with letter (?P<y>\w+)',
        'rotate direction left': 'rotate left (?P<x>\w+) step\.?',
        'rotate direction right': 'rotate right (?P<x>\w+) step\.?',
        'rotate position': 'rotate based on position of letter (?P<x>\w+)',
        'reverse position': 'reverse positions (?P<x>\w+) through (?P<y>\w+)',
        'move position': 'move position (?P<x>\w+) to position (?P<y>\w+)'
    }

    for instruction in ip_lines.split('\n'):
        for identifier, reg_expr in regular_expressions.items():
            y = re.search(reg_expr, instruction)
            if y:
                formatted_instructions.append((identifier, y.groups()))
                break
    return formatted_instructions


def get_unscrambled_str(ip_lines, password):
    s = list(password)
    if len(s) != 8:
        raise AssertionError("Can operate on 8 character string only")
    formatted_instructions = parse_instructions(ip_lines)[::-1]
    for instruction, params in formatted_instructions:
        if instruction == 'swap position':
            params = map(int, params)
            swap_position(s, params[0], params[1])
        elif instruction == 'swap letter':
            lookup = {params[0]: params[1], params[1]: params[0]}
            s = map(lambda x: lookup.get(x, x), list(s))
        elif instruction == 'rotate direction left':
            rotation_count = -int(params[0])
            s = s[rotation_count:] + s[:rotation_count]
        elif instruction == 'rotate direction right':
            rotation_count = int(params[0])
            s = s[rotation_count:] + s[:rotation_count]
        elif instruction == 'rotate position':
            char_position = s.index(params[0]) + 1
            if char_position % 2 == 0:
                char_position /= 2
            elif char_position != 1:
                char_position = (char_position + len(s)) / 2 + 1
            s = s[char_position:] + s[:char_position]
        elif instruction == 'reverse position':
            params = map(int, params)
            s = s[:params[0]] + s[params[0]:params[1] + 1][::-1] + s[params[1] + 1:]
        elif instruction == 'move position':
            params = map(int, params)
            s = move_postion(s, params[0], params[1])
    return ''.join(s)


def get_scrambled_password(ip_lines, ip):
    s = list(ip)
    formatted_instructions = parse_instructions(ip_lines)
    for instruction, params in formatted_instructions:
        if instruction == 'swap position':
            params = map(int, params)
            swap_position(s, params[0], params[1])
        elif instruction == 'swap letter':
            lookup = {params[0]: params[1], params[1]: params[0]}
            s = map(lambda x: lookup.get(x, x), list(s))
        elif instruction == 'rotate direction left':
            rotation_count = int(params[0])
            s = s[rotation_count:] + s[:rotation_count]
        elif instruction == 'rotate direction right':
            rotation_count = -int(params[0])
            s = s[rotation_count:] + s[:rotation_count]
        elif instruction == 'rotate position':
            rotation_count = s.index(params[0]) + 1
            if rotation_count > 4:
                rotation_count += 1
            rotation_count %= len(s)
            s = s[-rotation_count:] + s[:-rotation_count]
        elif instruction == 'reverse position':
            params = map(int, params)
            s = s[:params[0]] + s[params[0]:params[1] + 1][::-1] + s[params[1] + 1:]
        elif instruction == 'move position':
            params = map(int, params)
            s = move_postion(s, params[1], params[0])
    return ''.join(s)


ip_str = open('input.txt', 'r').read()
# a
print get_scrambled_password(ip_str, 'abcdefgh')
# b
print get_unscrambled_str(ip_str, 'fbgdceah')
