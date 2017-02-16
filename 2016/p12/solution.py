from pprint import pprint
from itertools import chain


def get_a_after_processing_instructions(instructions, a=0, b=0, c=0, d=0):
    registers = {'a': a, 'b': b, 'c': c, 'd': d}
    current_index = 0

    while True:
        if current_index >= len(instructions):
            break
        instruction_line = instructions[current_index]
        instruction, params = instruction_line
        if instruction == 'cpy':
            param1, param2 = params.split(' ')
            if param1 in registers:
                registers[param2] = registers[param1]
            else:
                registers[param2] = int(param1)
        if instruction == 'inc':
            registers[params] += 1
        if instruction == 'dec':
            registers[params] -= 1
        if instruction == 'jnz':
            param1, param2 = params.split(' ')
            if param1 in registers:
                if registers[param1] != 0:
                    current_index += int(param2)
                    continue
            elif param1 != '0':
                current_index += int(param2)
                continue
        current_index += 1
    return registers['a']


ip_str = open('input.txt', 'r').read()
f_ip = [l.split(' ', 1) for l in ip_str.split('\n')]
# a
print get_a_after_processing_instructions(f_ip)
# b
print get_a_after_processing_instructions(f_ip, c=1)