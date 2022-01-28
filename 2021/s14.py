class Solution(object):
	def __init__(self, input):
		polymer_str, polymer_rules = input.split('\n\n')
		self.current_polymer = {}
		self.extra_count = {}
		for i in range(len(polymer_str)-1):
			if polymer_str[i:i+2] not in self.current_polymer:
				self.current_polymer[polymer_str[i:i+2]] = 0
			self.current_polymer[polymer_str[i:i+2]] += 1
		self.rules = {}
		for polymer_rule in polymer_rules.splitlines():
			(s, e) = polymer_rule.split(' -> ')
			self.rules[s] = e

	def highestDifferencePair(self):
		char_lookup = {i:-self.extra_count[i] for i in self.extra_count}
		for key in self.current_polymer.keys():
			for k in list(key):
				if k not in char_lookup:
					char_lookup[k] = 0
				char_lookup[k] += self.current_polymer[key]
		sorted_chars = sorted(char_lookup.items(), key=lambda x: x[1])
		return (sorted_chars[-1][1]-sorted_chars[0][1])

	def runIterations(self, iterations=10):
		for i in range(iterations):
			new_polymer = {}
			for pair in self.current_polymer:
				if self.rules[pair] not in self.extra_count:
					self.extra_count[self.rules[pair]] = 0
				self.extra_count[self.rules[pair]] += self.current_polymer[pair]
				new_pairs = [pair[0]+self.rules[pair], self.rules[pair]+pair[1]]
				for p in new_pairs:
					if p not in new_polymer:
						new_polymer[p] = 0
					new_polymer[p] += self.current_polymer[pair]

			self.current_polymer = new_polymer


s = Solution('''CKKOHNSBPCPCHVNKHFFK

KO -> C
SO -> S
BF -> V
VN -> B
OV -> K
VH -> O
KV -> N
KB -> F
NB -> C
HS -> K
PF -> B
HB -> N
OC -> H
FS -> F
VV -> S
KF -> C
FN -> F
KP -> S
HO -> N
NH -> K
OO -> S
FB -> C
BP -> F
CH -> N
SN -> O
KN -> B
CV -> O
CC -> B
VB -> C
PH -> V
CO -> K
KS -> K
BK -> N
FH -> S
PV -> H
CB -> P
FO -> F
BB -> K
OB -> C
HH -> F
ON -> O
FK -> B
NF -> F
SV -> F
CP -> H
SS -> B
OP -> H
NS -> O
HK -> N
BC -> P
NV -> V
VS -> F
PC -> V
CS -> F
NP -> V
PS -> F
VC -> F
KK -> S
PO -> P
HF -> H
KC -> P
SF -> N
BV -> N
FF -> V
FV -> V
BO -> N
OS -> C
OF -> H
CN -> S
NO -> O
NC -> B
VK -> C
HN -> B
PK -> N
SK -> S
HV -> F
BH -> B
OK -> S
VO -> B
BS -> H
PP -> N
SC -> K
BN -> P
FC -> S
SB -> B
SH -> H
NN -> V
NK -> N
VF -> H
CF -> F
PB -> C
SP -> P
KH -> C
VP -> N
CK -> H
HP -> P
FP -> B
HC -> O
PN -> F
OH -> H''')
s.runIterations(10)
print(s.highestDifferencePair())
s.runIterations(30)
print(s.highestDifferencePair())
