class Solution(object):

	

	def __init__(self, input):
		self.instructions = []
		self.minz = 100000000000000
		self.memo = {}
		self.memo2 = {}
		current_instructions = []
		for line in input.splitlines():
			if 'inp' in line:
				if current_instructions:
					self.instructions.append(current_instructions)
				current_instructions = []
			current_instructions.append(line.split(' '))
		if current_instructions:
			self.instructions.append(current_instructions)

	def processInstructions(self, num, instructions_num, z_value):
		if (instructions_num, z_value, num) not in self.memo:
			variables = {'w': 0, 'x':0, 'y': 0, 'z': z_value}
			for instruction in self.instructions[instructions_num]:
				var = instruction[1]
				second_val = None
				if len(instruction) == 3:
					second_val = variables.get(instruction[2]) if instruction[2] in variables else int(instruction[2])
				if instruction[0] == 'inp':
					variables[var] = num
				if instruction[0] == 'add':
					variables[var] += second_val
				if instruction[0] == 'mul':
					variables[var] = variables[var] *  second_val
				if instruction[0] == 'div':
					variables[var] = int(variables[var] / second_val)
				if instruction[0] == 'mod':
					variables[var] = variables[var] % second_val
				if instruction[0] == 'eql':
					variables[var] = 1 if variables[var] == second_val else 0
			self.memo[(instructions_num,z_value, num)] = variables['z']
		return self.memo[(instructions_num, z_value, num)]

	def findPartA(self):
		return ''.join(map(str, self.findModelNum(0, 0, False)))

	def findPartB(self):
		return ''.join(map(str, self.findModelNum(0, 0)))

	
	def findModelNum(self, cur_index, z_val, forward_direction=True):
		key = f"{cur_index} {z_val}"
		if key in self.memo2:
			return self.memo2[key]
		result_nums = None
		order_nums = range(1, 10) if forward_direction else range(9, 0, -1)
		for i in order_nums:
			res = self.processInstructions(i, cur_index, z_val)
			if cur_index == 13:
				if abs(res) < self.minz:
					self.minz = abs(res)
				if res == 0:
					result_nums = [i]
					break
				else:
					result_nums = None
			else:
				new_num = self.findModelNum(cur_index + 1, res, forward_direction)
				if new_num:
					result_nums = [i] + new_num
					break
		self.memo2[key] = result_nums
		return result_nums


s = Solution('''inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y''')
print(s.findPartA())
print(s.findPartB())
