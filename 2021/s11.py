class Solution(object):
	def __init__(self, input):
		self.mat = []
		for l in input.splitlines():
			self.mat.append(map(int, list(l)))

	def printMatrix(self):
		for i in range(len(self.mat)):
			print(''.join(map(str, self.mat[i])))
		print ('\n')

	def findFlashes(self):
		c = 0
		for i in range(len(self.mat)):
			for j in range(len(self.mat[i])):
				if self.mat[i][j] == 0:
					c+= 1
		return c

	def executeFlash(self, i, j):
		future_flashes = []
		if self.mat[i][j] == 0:
			return
		if 	(i+1 < len(self.mat) and self.mat[i+1][j] > 0):
			self.mat[i+1][j]+=1
			if self.mat[i+1][j] > 9:
				future_flashes.append((i+1, j))
		if (i+1 < len(self.mat) and j+1 < len(self.mat[i]) and self.mat[i+1][j+1] > 0):
			self.mat[i+1][j+1]+=1
			if self.mat[i+1][j+1] > 9:
				future_flashes.append((i+1, j+1))
		if (i+1 < len(self.mat) and j >= 1 and self.mat[i+1][j-1] > 0):
			self.mat[i+1][j-1]+=1
			if self.mat[i+1][j-1] > 9:
				future_flashes.append((i+1, j-1))
 		if (i-1 >= 0 and j+1 < len(self.mat[i-1]) and self.mat[i-1][j+1] > 0):
 			 self.mat[i-1][j+1] += 1
 			 if self.mat[i-1][j+1] > 9:
				future_flashes.append((i-1, j+1))
		if (j+1 < len(self.mat[i]) and self.mat[i][j+1] > 0):
		 	 self.mat[i][j+1] += 1
		 	 if self.mat[i][j+1] > 9:
		 	 	future_flashes.append((i, j+1))
		if (j >= 1 and self.mat[i][j-1] > 0):
			self.mat[i][j-1] += 1
			if self.mat[i][j-1] > 9:
				future_flashes.append((i, j-1))
		if (i-1 >= 0 and j-1 >= 0 and self.mat[i-1][j-1] > 0):
			self.mat[i-1][j-1] += 1
			if self.mat[i-1][j-1] > 9:
				future_flashes.append((i-1, j-1))
		if (i >= 1 and self.mat[i-1][j] > 0):
			self.mat[i-1][j] += 1
			if self.mat[i-1][j] > 9:
				future_flashes.append((i-1, j))
		self.mat[i][j] = 0
		for (k,l) in future_flashes:
			self.executeFlash(k, l)

	def calculateFlashes(self, steps=100):
		total_flashes = 0
		for _ in range(steps):
			for i in range(len(self.mat)):
				for j in range(len(self.mat[i])):
					self.mat[i][j] += 1
			for i in range(len(self.mat)):
				for j in range(len(self.mat[i])):
					if self.mat[i][j] > 9:
						self.executeFlash(i, j)
			total_flashes += self.findFlashes()
		return total_flashes

	def getStepWhenAllFlashes(self):
		steps = 1
		total_octopuses = len(self.mat)*len(self.mat[0])
		while True:
			for i in range(len(self.mat)):
				for j in range(len(self.mat[i])):
					self.mat[i][j] += 1
			for i in range(len(self.mat)):
				for j in range(len(self.mat[i])):
					if self.mat[i][j] > 9:
						self.executeFlash(i, j)
			if total_octopuses == self.findFlashes():
				break
			steps += 1

		return steps


s = Solution('''4738615556
6744423741
2812868827
8844365624
4546674266
4518674278
7457237431
4524873247
3153341314
3721414667''')

print(s.calculateFlashes(100))

print(s.getStepWhenAllFlashes())


 
   
