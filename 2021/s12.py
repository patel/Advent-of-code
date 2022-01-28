import Queue
from collections import Counter
class Solution(object):
	def __init__(self, input):
		self.caves_lookup = {}
		for l in input.splitlines():
			a, b = l.split('-')
			if a not in self.caves_lookup:
				self.caves_lookup[a] = []
			if b not in self.caves_lookup:
				self.caves_lookup[b] = []
			self.caves_lookup[a].append(b)
			self.caves_lookup[b].append(a)

	def generatePath(self, node, prevPaths, predicate):
		if node == 'end':
			return prevPaths
		new_nodes =  self.caves_lookup[node]
		paths = []
		for n in new_nodes:
			if n == 'start':
				continue
			for prevPath in prevPaths:
				if predicate((n, prevPath)):
					continue
				paths = paths + self.generatePath(n, [prevPath + [n]], predicate)
		return paths

	def getPathsSizeA(self):
		nodes = self.caves_lookup['start']
		predicate = lambda (n, prevPath): n.lower() == n and n in prevPath
		paths = self.generatePath('start', [['start']], predicate)
		return len(paths)

	def getPathsSizeB(self):
		def _hasLowerDuplicatesExceptOne(l, n):
			lowerList = filter(lambda x: x.lower() == x, l)
			counts = Counter(lowerList)
			return (counts[n] == 2 or # at the most one duplicate present for n
				Counter(counts.values())[2] > 1) # at the most one duplicate present for any 
		predicate = lambda (n, prevPath): n.lower() == n and _hasLowerDuplicatesExceptOne(prevPath, n) 
		paths = self.generatePath('start', [['start']], predicate)
		return (len(paths))

s = Solution('''GC-zi
end-zv
lk-ca
lk-zi
GC-ky
zi-ca
end-FU
iv-FU
lk-iv
lk-FU
GC-end
ca-zv
lk-GC
GC-zv
start-iv
zv-QQ
ca-GC
ca-FU
iv-ca
start-lk
zv-FU
start-zi''')
#print(s.getPathsSizeA())
print(s.getPathsSizeB())

