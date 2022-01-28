from functools import lru_cache
class Solution(object):

	def __init__(self, player1, player2):
		self.player1_pos = player1
		self.player2_pos = player2
		self.player1_score = 0
		self.player2_score = 0
		self.roll_start = 0
		self.roll_counter = 0

	def playA(self, player_pos):
		scores = sum([(self.roll_start + i) for i in range(1,4)])
		player_pos = (player_pos + scores) % 10 or 10
		self.roll_counter += 3
		self.roll_start += 3
		return player_pos


	def runA(self):
		while True:
			self.player1_pos = self.playA(self.player1_pos)
			self.player1_score += self.player1_pos
			if self.player1_score >= 1000: 
				return self.player2_score * self.roll_counter
			self.player2_pos = self.playA(self.player2_pos)
			self.player2_score += self.player2_pos
			if self.player2_score >= 1000:
				return self.player1_score * self.roll_counter

	@lru_cache(maxsize=None)
	def runB(self, position_a, position_b, score_a, score_b):
		if score_a >= 21:
			return [1, 0]
		if score_b >= 21:
			return [0, 1]


		scores = [0, 0]
		for score1 in [1,2,3]:
			for score2 in [1,2,3]:
				for score3 in [1,2,3]:
					new_score = score1 + score2 + score3
					new_position_a = (position_a + new_score) % 10 or 10
					new_score_a = score_a + new_position_a 
					if new_score_a >= 21:
						scores[0] += 1
					else:
						for scoreb1 in [1,2,3]:
							for scoreb2 in [1,2,3]:
								for scoreb3 in [1,2,3]:
									new_score_b = scoreb1 + scoreb2 + scoreb3
									new_position_b = (position_b + new_score_b) % 10 or 10
									new_score_b = score_b + new_position_b
									if new_score_b >= 21:
										scores[1] = scores[1] + 1
									else:
										score = self.runB(new_position_a, new_position_b, new_score_a, new_score_b)
										scores[0] = scores[0] + score[0] 
										scores[1] = scores[1] + score[1]
		return scores

s = Solution(4, 6)
print(s.runA())
print(max(s.runB(4, 6, 0, 0)))
