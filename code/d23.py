def execute_program(program_lines, initial_values):
    i = 0
    registers = initial_values
    while (i < len(program_lines)):
        program_line = program_lines[i]
        offset = 1
        instruction = program_line[:3]
        if instruction == 'hlf':
            registers[program_line[4]] = registers[program_line[4]] / 2
        elif instruction == 'tpl':
            registers[program_line[4]] = registers[program_line[4]] * 3
        elif instruction == 'inc':
            registers[program_line[4]] = registers[program_line[4]] + 1
        elif instruction == 'jmp':
            offset = int(program_line[4:])
        elif instruction == 'jie' or instruction == 'jio':
            value = registers[program_line[4]]
            if (instruction == 'jio' and value == 1) or (instruction == 'jie' and value % 2 is 0):
                offset = int(program_line[7:])
        i = i + offset

    return registers['b']

instructions = [
'jio a, +19',
'inc a',
'tpl a',
'inc a',
'tpl a',
'inc a',
'tpl a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'jmp +23',
'tpl a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'inc a',
'tpl a',
'inc a',
'tpl a',
'inc a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'inc a',
'inc a',
'tpl a',
'tpl a',
'inc a',
'jio a, +8',
'inc b',
'jie a, +4',
'tpl a',
'inc a',
'jmp +2',
'hlf a',
'jmp -7']

print execute_program(instructions, {'a': 0 , 'b': 0})
print execute_program(instructions, {'a': 1 , 'b': 0})