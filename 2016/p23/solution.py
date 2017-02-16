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
            elif param2 in registers:
                registers[param2] = int(param1)
        if instruction == 'inc':
            registers[params] += 1
        if instruction == 'dec':
            registers[params] -= 1
        if instruction == 'jnz':
            param1, param2 = params.split(' ')
            jmp_cnt = registers[param2] if param2 in registers else int(param2)
            if (param1 in registers and registers[param1] != 0) or (param1 not in registers and param1 != '0'):
                current_index += jmp_cnt
                if jmp_cnt < 0:
                    if all(map(lambda x: x[0] in ['inc', 'dec'], instructions[current_index:current_index-jmp_cnt])):
                        for l_inst, l_param in instructions[current_index:current_index - jmp_cnt]:
                            if l_param == param1:
                                continue
                            if l_inst == 'inc':
                                registers[l_param] += abs(registers[param1])
                            else:
                                registers[l_param] -= abs(registers[param1])
                        registers[param1] = 0
                        current_index -= (jmp_cnt)
                        current_index += 1
                continue
        if instruction == 'tgl':
            jmp_cnt = registers[params]
            if 0 <= current_index+jmp_cnt < len(instructions):
                instruction_toggle, params_toggle = instructions[current_index+jmp_cnt]
                params_list = params_toggle.split(' ')
                if len(params_list) == 1:
                    instructions[current_index + jmp_cnt][0] = {'inc': 'dec'}.get(instruction_toggle, 'inc')
                if len(params_list) == 2:
                    instructions[current_index + jmp_cnt][0] = {'jnz': 'cpy'}.get(instruction_toggle, 'jnz')
        current_index += 1
    return registers['a']


ip = open('input.txt', 'r').read()

f_ip = [l.split(' ', 1) for l in ip.split('\n')]
print get_a_after_processing_instructions(f_ip, a=7)
f_ip = [l.split(' ', 1) for l in ip.split('\n')]
print get_a_after_processing_instructions(f_ip, a=12)