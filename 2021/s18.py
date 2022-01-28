class Pair(object):
		def __init__(self, input):
			self.elements = []
			self._is_plain_pair = False
			self.parent = None
			is_list_found = False
			for n in input:
				if type(n) is list:
					new_pair = Pair(n)
					self.elements.append(new_pair)
					new_pair.parent = self
					is_list_found = True
				else:
					self.elements.append(n)
			self._is_plain_pair = not is_list_found

		def get_exploding_pair(self, cnt=1):
			for element in self.elements:
				if cnt <= 1:
					if type(element) is Pair and element._is_plain_pair:
						return element
				else:
					if type(element) is Pair:
						new_element = element.get_exploding_pair(cnt-1)
						if new_element:
							return new_element

		def __str__(self):
			return "[" + ",".join([str(e) for e in self.elements]) + "]" 

class Solution(object):
	
	def parse(self, input):
		self.parsed_output = []
		s = []
		for c in list(input):
			if c == '[':
				s.append('[')
			elif c == ']':
				current_number = []
				while s[-1] != '[':
					current_number.append(s.pop())
				s.pop()
				if current_number:
					s.append(current_number[::-1])
			elif c != ',':

				s.append(int(c) if ord(c) >= 48 and ord(c) < 58 else c)
		return s

	
	def __init__(self, input):
		self.input = input.splitlines()
		self.instructions = []
		for line in input.splitlines():
			self.instructions.append(Pair(self.parse(line)))

	def process_2(self):
		pass

	def process_instruction(self, line):
		s = []
		cnt = 0
		right = 0
		for c in list(line):
			print('cnt', cnt)
			if c == '[':
				cnt += 1
				s.append('[')
			elif c == ']':
				current_number = []
				while s[-1] != '[':
					current_number.append(s.pop())
				s.pop()
				if current_number:
					if cnt > 4 and type(current_number) is list and len(current_number) == 2 and not any([type(i) is list for i in current_number]):
						is_processed = True
						print('processing ', current_number, is_processed)
						left = [0]
						right = current_number[0]
						while s:
							c = s.pop()
							if type(c) is int:
								c += current_number[1]
								print('s before ', s)	
								s = s+ left[::-1]
								left = []
								current_number = []
								cnt -= 1
								break
							else:
								left.append(c)
						if left:
							s = s + left[::-1]
					else:
						s.append(current_number[::-1])
				else:
					s.append(current_number[::-1])
				cnt -= 1
			elif type(c) is int and c >= 10:
				s.append([int(c/2), c-int(c/2)])
			elif c != ',':
				s.append(int(c) if ord(c) >= 48 and ord(c) < 58 else c)
				if type(s[-1]) is int and right > 0:
					s[-1] += right
					right = 0
			print(s)


	def process(self):
		final_num = []
		for instruction in self.parsed_output:
			final_num = final_num + instruction
			new_instruction.append(instruction[i:])
			existing_instructions.append(instruction)
		print(existing_instructions)

s = Solution('''[7,[6,[5,[4,[3,2]]]]]''')
#s = Solution('''[1,1]''')

#print(s.instructions)
for ins in s.instructions:
	print(ins.get_exploding_pair(5))


