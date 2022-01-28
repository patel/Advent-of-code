import re 
class Solution(object):

	def __init__(self, input):
		self.scanner_lookup = {}
		scan_id = -1	
		for line in input.splitlines():
			scan_match = re.match(r"--- scanner (?P<scanid>\d+) ---", line)
			if scan_match:
				scan_id = int(scan_match.group('scanid'))
				self.scanner_lookup[scan_id] = []
			elif line == '':
				continue
			else:
				self.scanner_lookup[scan_id].append(map(int, line.split(',')))

	
	def _HasMatchingBeacons(self, items1Set, items2Set):
		s = {}
		for item in items1Set:
			for item2 in items2Set:
				candidates = [{(('-', '-', '-'), ((0, 0), (1, 1), (2, 2))) :(item[0]-item2[0], item[1]-item2[1], item[2]-item2[2]), 
							 (('-', '-', '+'), ((0, 0), (1, 1), (2, 2))): (item[0]-item2[0], item[1]-item2[1], item[2]+item2[2]), 
							 (('-', '+', '-'), ((0, 0), (1, 1), (2, 2))): (item[0]-item2[0], item[1]+item2[1], item[2]-item2[2]),
							 (('+', '-', '-'), ((0, 0), (1, 1), (2, 2))): (item[0]+item2[0], item[1]-item2[1], item[2]-item2[2]), 
							 (('+', '+', '-'), ((0, 0), (1, 1), (2, 2))): (item[0]+item2[0], item[1]+item2[1], item[2]-item2[2]), 
							 (('+', '-', '+'), ((0, 0), (1, 1), (2, 2))): (item[0]+item2[0], item[1]-item2[1], item[2]+item2[2]), 
							 (('-', '+', '+'), ((0, 0), (1, 1), (2, 2))): (item[0]-item2[0], item[1]+item2[1], item[2]+item2[2]),
							 (('+', '+', '+'), ((0, 0), (1, 1), (2, 2))): (item[0]+item2[0], item[1]+item2[1], item[2]+item2[2])}, 

							  {(('-', '-', '-'),((0, 0), (1, 2), (2, 1))) :(item[0]-item2[0], item[1]-item2[2], item[2]-item2[1]), 
							  (('-', '-', '+'), ((0, 0), (1, 2), (2, 1))):(item[0]-item2[0], item[1]-item2[2], item[2]+item2[1]), 
							  (('-', '+', '-'), ((0, 0), (1, 2), (2, 1))): (item[0]-item2[0], item[1]+item2[2], item[2]-item2[1]),
							  (('+', '-', '-'), ((0, 0), (1, 2), (2, 1))):(item[0]+item2[0], item[1]-item2[2], item[2]-item2[1]), 
							  (('+', '+', '-'), ((0, 0), (1, 2), (2, 1))):(item[0]+item2[0], item[1]+item2[2], item[2]-item2[1]), 
							  (('+', '-', '+'), ((0, 0), (1, 2), (2, 1))): (item[0]+item2[0], item[1]-item2[2], item[2]+item2[1]), 
							  (('-', '+', '+'), ((0, 0), (1, 2), (2, 1))):(item[0]-item2[0], item[1]+item2[2], item[2]+item2[1]),
							  (('+', '+', '+'), ((0, 0), (1, 2), (2, 1))): (item[0]+item2[0], item[1]+item2[2], item[2]+item2[1])}, 

							  {(('-', '-', '-'), ((0, 1), (1, 2), (2, 0))) :(item[0]-item2[1], item[1]-item2[2], item[2]-item2[0]), 
							  (('-', '-', '+'),  ((0, 1), (1, 2), (2, 0))):(item[0]-item2[1], item[1]-item2[2], item[2]+item2[0]), 
							  (('-', '+', '-'),  ((0, 1), (1, 2), (2, 0))):(item[0]-item2[1], item[1]+item2[2], item[2]-item2[0]),
							  (('+', '-', '-'),  ((0, 1), (1, 2), (2, 0))):(item[0]+item2[1], item[1]-item2[2], item[2]-item2[0]), 
							  (('+', '+', '-'),  ((0, 1), (1, 2), (2, 0))):(item[0]+item2[1], item[1]+item2[2], item[2]-item2[0]), 
							  (('+', '-', '+'),  ((0, 1), (1, 2), (2, 0))): (item[0]+item2[1], item[1]-item2[2], item[2]+item2[0]), 
							  (('-', '+', '+'),  ((0, 1), (1, 2), (2, 0))):(item[0]-item2[1], item[1]+item2[2], item[2]+item2[0]),
							  (('+', '+', '+'),  ((0, 1), (1, 2), (2, 0))): (item[0]+item2[1], item[1]+item2[2], item[2]+item2[0])}, 

							  {(('-', '-', '-'), ((0, 1), (1, 0), (2, 2))) :(item[0]-item2[1], item[1]-item2[0], item[2]-item2[2]), 
							  (('-', '-', '+'), ((0, 1), (1, 0), (2, 2))):(item[0]-item2[1], item[1]-item2[0], item[2]+item2[2]), 
							  (('-', '+', '-'), ((0, 1), (1, 0), (2, 2))):(item[0]-item2[1], item[1]+item2[0], item[2]-item2[2]),
							  (('+', '-', '-'), ((0, 1), (1, 0), (2, 2))):(item[0]+item2[1], item[1]-item2[0], item[2]-item2[2]), 
							  (('+', '+', '-'), ((0, 1), (1, 0), (2, 2))):(item[0]+item2[1], item[1]+item2[0], item[2]-item2[2]), 
							  (('+', '-', '+'), ((0, 1), (1, 0), (2, 2))): (item[0]+item2[1], item[1]-item2[0], item[2]+item2[2]), 
							  (('-', '+', '+'), ((0, 1), (1, 0), (2, 2))):(item[0]-item2[1], item[1]+item2[0], item[2]+item2[2]),
							  (('+', '+', '+'), ((0, 1), (1, 0), (2, 2))): (item[0]+item2[1], item[1]+item2[0], item[2]+item2[2])}, 	

							  {(('-', '-', '-'), ((0, 2), (1, 1), (2, 0))) :(item[0]-item2[2], item[1]-item2[1], item[2]-item2[0]), 
							  (('-', '-', '+'), ((0, 2), (1, 1), (2, 0))):(item[0]-item2[2], item[1]-item2[1], item[2]+item2[0]), 
							  (('-', '+', '-'), ((0, 2), (1, 1), (2, 0))): (item[0]-item2[2], item[1]+item2[1], item[2]-item2[0]),
							  (('+', '-', '-'), ((0, 2), (1, 1), (2, 0))):(item[0]+item2[2], item[1]-item2[1], item[2]-item2[0]), 
							  (('+', '+', '-'), ((0, 2), (1, 1), (2, 0))):(item[0]+item2[2], item[1]+item2[1], item[2]-item2[0]), 
							  (('+', '-', '+'), ((0, 2), (1, 1), (2, 0))): (item[0]+item2[2], item[1]-item2[1], item[2]+item2[0]), 
							  (('-', '+', '+'), ((0, 2), (1, 1), (2, 0))):(item[0]-item2[2], item[1]+item2[1], item[2]+item2[0]),
							  (('+', '+', '+'), ((0, 2), (1, 1), (2, 0))): (item[0]+item2[2], item[1]+item2[1], item[2]+item2[0])}, 

							  {(('-', '-', '-'), ((0, 2), (1, 0), (2, 1))) :(item[0]-item2[2], item[1]-item2[0], item[2]-item2[1]), 
							  (('-', '-', '+'), ((0, 2), (1, 0), (2, 1))): (item[0]-item2[2], item[1]-item2[0], item[2]+item2[1]), 
							  (('-', '+', '-'), ((0, 2), (1, 0), (2, 1))): (item[0]-item2[2], item[1]+item2[0], item[2]-item2[1]),
							  (('+', '-', '-'), ((0, 2), (1, 0), (2, 1))): (item[0]+item2[2], item[1]-item2[0], item[2]-item2[1]), 
							  (('+', '+', '-'), ((0, 2), (1, 0), (2, 1))): (item[0]+item2[2], item[1]+item2[0], item[2]-item2[1]), 
							  (('+', '-', '+'), ((0, 2), (1, 0), (2, 1))): (item[0]+item2[2], item[1]-item2[0], item[2]+item2[1]), 
							  (('-', '+', '+'), ((0, 2), (1, 0), (2, 1))): (item[0]-item2[2], item[1]+item2[0], item[2]+item2[1]),
							  (('+', '+', '+'), ((0, 2), (1, 0), (2, 1))): (item[0]+item2[2], item[1]+item2[0], item[2]+item2[1])}, 
							  ]
				for (i, dictionary) in enumerate(candidates):
					for sign_direction, candidate in dictionary.items():
						sign, direction = sign_direction
						if i not in s:
							s[i] = {}
						if candidate not in s[i]:
							s[i][candidate] = 0
						s[i][candidate] += 1
						if s[i][candidate] >= 12:
							return True, (sign, direction, candidate)
		return False, ()

	def findBeacons(self):
		scanners = self.scanner_lookup.keys()
		relative_positions = {}

		for i in range(len(scanners)):
			for j in range(len(scanners)):
				if i == j:
					continue
				is_matching, matching_repsonse = self._HasMatchingBeacons(self.scanner_lookup[scanners[i]], self.scanner_lookup[scanners[j]])
				if is_matching:
					sign, direction, common_index = matching_repsonse
					if i not in relative_positions:
						relative_positions[i] = {}
					relative_positions[i][j] = (common_index, sign, direction)

				 	
		for (k, v) in relative_positions.items():
			print(k, '->', v)
		absolute_positions = {0: ((0,0,0), ('+', '+', '+'), ((0, 0), (1, 1), (2, 2)))}
		for k, v in relative_positions[0].items():
			absolute_positions[k] = v
		for i in relative_positions:
			for j in relative_positions[i]:
				if j in absolute_positions:
					continue
				if i in absolute_positions:
					relative_position, sign, direction = relative_positions[i][j]
					absolute_position, absolute_sign, absolute_direction = absolute_positions[i]
					
					print ('relative ', i, j, absolute_position, absolute_sign, absolute_direction, relative_position, sign, direction)
					
					relative_dir_lookup = {direction[d][1]: direction[d][0] for d in range(3)}
					relative_opp_dir_lookup = {direction[d][0]: direction[d][1] for d in range(3)}
					absolute_dir_lookup = {absolute_direction[d][0]: absolute_direction[d][1] for d in range(3)}

					relative_pos_lookup = {direction[d][0]: d for d in range(3)}

					def get_sign_direction(a_sign, b_sign):
						if a_sign == '+' and b_sign == '+':
							return ('-', '-')
						if a_sign == '+' and b_sign == '-':
							return ('-', '+')
						if a_sign == '-' and b_sign == '+':
							return ('+', '+')
						if a_sign == '-' and b_sign == '-':
							return ('+', '-')

					def perform_operation(a, b, sign):
						if sign == '+':
							return a+b
						else:
							return a-b

					new_directions = []
					new_vals = []
					new_signs = []
					for k in range(3):
						new_operator, new_sign = get_sign_direction(absolute_sign[k], sign[k])
						print('processing ', absolute_position[k], relative_position[relative_pos_lookup[absolute_dir_lookup[k]]], new_operator)
						new_vals.append(perform_operation(absolute_position[k], relative_position[relative_pos_lookup[absolute_dir_lookup[k]]], new_operator))
						new_signs.append(new_sign)
						new_directions.append((k, relative_opp_dir_lookup[k]))
						
					absolute_positions[j] = (tuple(new_vals), tuple(new_signs), tuple(new_directions))
					print ('absolute_positions[j]', j, absolute_positions[j])

		final_answers =set(map(tuple, [[-892,524,684],
[-876,649,763],
[-838,591,734],
[-789,900,-551],
[-739,-1745,668],
[-706,-3180,-659],
[-697,-3072,-689],
[-689,845,-530],
[-687,-1600,576],
[-661,-816,-575],
[-654,-3158,-753],
[-635,-1737,486],
[-631,-672,1502],
[-624,-1620,1868],
[-620,-3212,371],
[-618,-824,-621],
[-612,-1695,1788],
[-601,-1648,-643],
[-584,868,-557],
[-537,-823,-458],
[-532,-1715,1894],
[-518,-1681,-600],
[-499,-1607,-770],
[-485,-357,347],
[-470,-3283,303],
[-456,-621,1527],
[-447,-329,318],
[-430,-3130,366],
[-413,-627,1469],
[-345,-311,381],
[-36,-1284,1171],
[-27,-1108,-65],
[7,-33,-71],
[12,-2351,-103],
[26,-1119,1091],
[346,-2985,342],
[366,-3059,397],
[377,-2827,367],
[390,-675,-793],
[396,-1931,-563],
[404,-588,-901],
[408,-1815,803],
[423,-701,434],
[432,-2009,850],
[443,580,662],
[455,729,728],
[456,-540,1869],
[459,-707,401],
[465,-695,1988],
[474,580,667],
[496,-1584,1900],
[497,-1838,-617],
[527,-524,1933],
[528,-643,409],
[534,-1912,768],
[544,-627,-890],
[553,345,-567],
[564,392,-477],
[568,-2007,-577],
[605,-1665,1952],
[612,-1593,1893],
[630,319,-379],
[686,-3108,-505],
[776,-3184,-501],
[846,-3110,-434],
[1135,-1161,1235],
[1243,-1093,1063],
[1660,-552,429],
[1693,-557,386],
[1735,-437,1738],
[1749,-1800,1813],
[1772,-405,1572],
[1776,-675,371],
[1779,-442,1789],
[1780,-1548,337],
[1786,-1538,337],
[1847,-1591,415],
[1889,-1729,1762],
[1994,-1805,1792]]))

		all_points = set()
		for i in [0,1,3,4,2]:
			points = self.scanner_lookup[i]
			if i == 0:
				all_points = set(map(tuple, points))
			else:

				new_points = set()
				print('processing', i, absolute_positions[i])
				(abs_position, sign, direction) = absolute_positions[i]
				if i == 2:
					direction = ((0,0), (1,1), (2,2))
					sign = ('-','-', '+')
				index_lookup = {i:j for i, j in direction}
				for point in points:
					new_point = ( abs_position[0]- (1 if sign[0] == '+' else -1) * point[index_lookup[0]], 
								  abs_position[1]- (1 if sign[1] == '+' else -1) * point[index_lookup[1]], 
								  abs_position[2]- (1 if sign[2] == '+' else -1) * point[index_lookup[2]])
					if point[0] == -675:
						print ('-675 ', point, direction, sign)
					#print ('point ', point, 'new_point ', new_point)
					new_points.add(new_point)
				print('for scanner', i)
				all_points = all_points.union(new_points)
				for p in sorted(new_points - final_answers):
						print ('coming ', i, p)
				if i == 2:
					for p in sorted(final_answers - all_points):
						print ('coming again', i, p)
						
			print(len(all_points))

s = Solution('''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14''')
s.findBeacons()