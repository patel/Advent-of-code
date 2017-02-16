from collections import defaultdict
from itertools import chain
from pprint import pprint


def get_a_after_processing_instructions_a(instructions, a=0, b=0, c=0, d=0):
    registers = {'a': a, 'b': b, 'c': c, 'd': d}
    current_index = 0
    prev_out = 1
    circled_once = False
    registers_lookup = defaultdict(list)
    while True:
        if current_index >= len(instructions):
            break
        if current_index == len(instructions) - 1:
            circled_once = True

        instruction_line = instructions[current_index]
        instruction, params = instruction_line
        if instruction == 'cpy':
            param1, param2 = params.split(' ')
            if param1 in registers:
                registers[param2] = registers[param1]
            elif param2 in registers:
                registers[param2] = int(param1)
        if instruction == 'inc':
            registers[params] += 1
        if instruction == 'dec':
            registers[params] -= 1
        if instruction == 'jnz':
            param1, param2 = params.split(' ')
            jmp_cnt = registers[param2] if param2 in registers else int(param2)
            if param1 in registers:
                if registers[param1] != 0:
                    current_index += jmp_cnt
                    continue
            elif param1 != '0':
                current_index += jmp_cnt
                continue
        if instruction == 'out':
            if (params in registers and registers[params] != 1 - prev_out) or \
                    (params not in registers and params != 1 - prev_out):
                return False
            else:
                prev_out = registers[params] if params in registers else params
        if instruction == 'tgl':
            jmp_cnt = registers[params]
            if 0 <= current_index + jmp_cnt < len(instructions):
                instruction_toggle, params_toggle = instructions[current_index + jmp_cnt]
                params_list = params_toggle.split(' ')
                if len(params_list) == 1:
                    instructions[current_index + jmp_cnt][0] = {'inc': 'dec'}.get(instruction_toggle, 'inc')
                if len(params_list) == 2:
                    instructions[current_index + jmp_cnt][0] = {'jnz': 'cpy'}.get(instruction_toggle, 'jnz')
        if circled_once and registers in registers_lookup[current_index]:
            return True
        registers_lookup[current_index].append(registers)
        current_index += 1
    return registers['a']


ip = open('input.txt', 'r').read()

f_ip = [l.split(' ', 1) for l in ip.split('\n')]
k = 1
while True:
    if get_a_after_processing_instructions_a(f_ip, a=k):
        print k
        break
    else:
        k += 1
