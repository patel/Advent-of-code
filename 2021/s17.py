import re 
class Solution(object):

	def __init__(self, input, is_binary=False):
		m = re.match(r"target area\: x\=(?P<x1>.*)\.\.(?P<x2>.*)\, y\=(?P<y1>.*)\.\.(?P<y2>.*)", input)
		if m:
			self.x1 = int(m.group('x1'))
			self.x2 = int(m.group('x2'))
			self.y1 = int(m.group('y1'))
			self.y2 = int(m.group('y2'))

	def doesHitTarget(self, vx, vy):
		s = 1
		x,y = 0,0
		while True:
			x += vx
			y += vy
			vx = vx - 1 if vx > 0 else 0
			vy = vy - 1
			if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2: 
				return True
			if x > self.x2:
				break
			if y < self.y1:
				break
		return False

	def calcMaxYValue(self):
		max_x_y = self.calcMaxValue()
		y = max_x_y[1]
		return y * (y+1)/2

	def calcAllVelocities(self):
		all_velocities = []
		for x in range(self.x2+1):
			y = self.y1 
			while True:
				if self.doesHitTarget(x, y):
					all_velocities.append((x, y))
				if y > -self.y1:
					break
				y += 1
				
		return all_velocities

	def calcMaxValue(self):
		min_x = int((self.x1*2)**.5)
		max_x = int((self.x2*2)**.5)
		max_x_y = (0,0)
		for x in range(min_x, max_x+1):
			y = 0
			while True:
				if self.doesHitTarget(x, y):
					if y > max_x_y[1]:
						max_x_y = (x, y)
				y += 1
				if y > -self.y1:
					break
		return max_x_y

s = Solution("target area: x=241..273, y=-97..-63")
print(s.calcMaxYValue())
print(len(s.calcAllVelocities()))