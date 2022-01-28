import functools 
class Packet(object):

	def __init__(self, input, is_binary=False):
		if is_binary:
			self.binary_string = input
		else:
			self.binary_string = ''.join(['{:04b}'.format(int(k, 16)) for k in list(input)]).replace('0b', '')
		self.packet_version = int(self.binary_string[:3], 2)
		self.packet_type_id = int(self.binary_string[3:6], 2)
		self.subpackets = []
		self.literal_int = 0
		self.size = 6
		if self.packet_type_id == 4:
			literal_value = self.binary_string[6:]
			literal_int = 0
			while literal_value:
				current_literal = int(literal_value[:5], 2)
				literal_value = literal_value[5:]
				literal_int = literal_int * 16 + (current_literal & 15)
				self.size += 5
				if (not current_literal & 16):
					break	
			self.literal_int = literal_int
		else:
			self.length_type_id = int(self.binary_string[6], 2)
			if self.length_type_id == 0:
				i = 22
				length_subpackets = int(self.binary_string[7:22], 2)
				self.size = 22 + length_subpackets
				while length_subpackets > 0:
					p = Packet(self.binary_string[i:], is_binary=True)
					self.subpackets.append(p)
					i += p.size
					length_subpackets -= p.size
				self.size = i
			else:
				num_subpackets =  int(self.binary_string[7:18], 2)
				i = 18
				while num_subpackets > 0:
					p = Packet(self.binary_string[i:], is_binary=True)
					self.subpackets.append(p)
					i += p.size
					num_subpackets -= 1
				self.size = i
					
			
	def calcSumVersions(self):
		version = 0
		for subpacket in self.subpackets:
			subpacket_sum =  subpacket.calcSumVersions()
			version += subpacket_sum
		return self.packet_version + version

	def calcValues(self):
		if self.packet_type_id == 0:
			return sum([x.calcValues() for x in self.subpackets])
		elif self.packet_type_id == 1:
			return functools.reduce(lambda a, b: a*b, [x.calcValues() for x in self.subpackets])
		elif self.packet_type_id == 2:
			return min([x.calcValues() for x in self.subpackets])
		elif self.packet_type_id == 3:	
			return max([x.calcValues() for x in self.subpackets])
		elif self.packet_type_id == 5:	
			return 1 if self.subpackets[0].calcValues() > self.subpackets[1].calcValues() else 0
		elif self.packet_type_id == 6:	
			return 1 if self.subpackets[0].calcValues() < self.subpackets[1].calcValues() else 0
		elif self.packet_type_id == 7:	
			return 1 if self.subpackets[0].calcValues() == self.subpackets[1].calcValues() else 0
		elif self.packet_type_id == 4:
			return self.literal_int


s = Packet('A059141803C0008447E897180401F82F1E60D80021D11A3DC3F300470015786935BED80A5DB5002F69B4298A60FE73BE41968F48080328D00427BCD339CC7F431253838CCEFF4A943803D251B924EC283F16D400C9CDB3180213D2D542EC01092D77381A98DA89801D241705C80180960E93469801400F0A6CEA7617318732B08C67DA48C27551C00F972830052800B08550A277416401A5C913D0043D2CD125AC4B1DB50E0802059552912E9676931530046C0141007E3D4698E20008744D89509677DBF5759F38CDC594401093FC67BACDCE66B3C87380553E7127B88ECACAD96D98F8AC9E570C015C00B8E4E33AD33632938CEB4CD8C67890C01083B800E5CBDAB2BDDF65814C01299D7E34842E85801224D52DF9824D52DF981C4630047401400042E144698B2200C4328731CA6F9CBCA5FBB798021259B7B3BBC912803879CD67F6F5F78BB9CD6A77D42F1223005B8037600042E25C158FE0008747E8F50B276116C9A2730046801F29BC854A6BF4C65F64EB58DF77C018009D640086C318870A0C01D88105A0B9803310E2045C8CF3F4E7D7880484D0040001098B51DA0980021F17A3047899585004E79CE4ABD503005E610271ED4018899234B64F64588C0129EEDFD2EFBA75E0084CC659AF3457317069A509B97FB3531003254D080557A00CC8401F8791DA13080391EA39C739EFEE5394920C01098C735D51B004A7A92F6A0953D497B504F200F2BC01792FE9D64BFA739584774847CE26006A801AC05DE180184053E280104049D10111CA006300E962005A801E2007B80182007200792E00420051E400EF980192DC8471E259245100967FF7E6F2CF25DBFA8593108D342939595454802D79550C0068A72F0DC52A7D68003E99C863D5BC7A411EA37C229A86EBBC0CB802B331FDBED13BAB92080310265296AFA1EDE8AA64A0C02C9D49966195609C0594223005B80152977996D69EE7BD9CE4C1803978A7392ACE71DA448914C527FFE140')
print(s.calcSumVersions())
print(s.calcValues())
