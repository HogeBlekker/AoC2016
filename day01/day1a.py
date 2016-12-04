class Walker(object):
	def __init__(self, start_x, start_y):
		self.x = start_y
		self.y = start_y
		self.current_direction = 1 # 1 = N, 2 = E, 3 = S, 4 = W

	def set_course(self, aim):
		if aim == 'R':
			if self.current_direction != 4:
				self.current_direction += 1
			else:
				self.current_direction = 1
		else:
			if self.current_direction != 1:
				self.current_direction -= 1
			else:
				self.current_direction = 4

	def set_steps(self, distance):
		if self.current_direction == 1:
			self.y = self.y+distance
		elif self.current_direction == 2:
			self.x = self.x+distance
		elif self.current_direction == 3:
			self.y = self.y-distance
		else:
			self.x = self.x-distance

instructions = 'R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3'
#instructions = 'R2, L3'
#instructions = 'R2, R2, R2'
#instructions = 'R5, L5, R5, R3'
instructions = instructions.split(', ')

origin_x = 1000
origin_y = 1000
santa = Walker(origin_x, origin_y)

for step in instructions:
	aim = step[0:1]
	distance = int(step[1:])
	santa.set_course(aim)
	santa.set_steps(distance)

print "Final X: %d" % santa.x
print "Final Y: %d" % santa.y
total_distance = abs(origin_y - santa.y) + abs(origin_x - santa.x)
print "Distance: %d" % total_distance
