import re

# input = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1"""

input = """rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 5
rotate row y=0 by 3
rect 1x2
rotate column x=30 by 1
rotate column x=25 by 1
rotate column x=10 by 1
rotate row y=1 by 5
rotate row y=0 by 2
rect 1x2
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 18
rotate row y=0 by 5
rotate column x=0 by 1
rect 3x1
rotate row y=2 by 12
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=20 by 1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 15
rotate row y=0 by 15
rotate column x=10 by 1
rotate column x=5 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=37 by 1
rotate column x=23 by 1
rotate column x=7 by 2
rotate row y=3 by 20
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 5
rotate row y=2 by 2
rotate row y=1 by 4
rotate row y=0 by 4
rect 1x4
rotate column x=35 by 3
rotate column x=18 by 3
rotate column x=13 by 3
rotate row y=3 by 5
rotate row y=2 by 3
rotate row y=1 by 1
rotate row y=0 by 1
rect 1x5
rotate row y=4 by 20
rotate row y=3 by 10
rotate row y=2 by 13
rotate row y=0 by 10
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 10
rotate row y=3 by 10
rotate row y=1 by 10
rotate row y=0 by 10
rotate column x=7 by 2
rotate column x=5 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 20
rotate row y=3 by 12
rotate row y=1 by 15
rotate row y=0 by 10
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=6 by 2
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=46 by 2
rotate column x=43 by 2
rotate column x=24 by 2
rotate column x=14 by 3
rotate row y=5 by 15
rotate row y=4 by 10
rotate row y=3 by 3
rotate row y=2 by 37
rotate row y=1 by 10
rotate row y=0 by 5
rotate column x=0 by 3
rect 3x3
rotate row y=5 by 15
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=7 by 3
rotate column x=6 by 3
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=19 by 1
rotate column x=10 by 3
rotate column x=5 by 4
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 40
rotate row y=2 by 35
rotate row y=1 by 15
rotate row y=0 by 30
rotate column x=48 by 4
rotate column x=47 by 3
rotate column x=46 by 3
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=42 by 5
rotate column x=41 by 5
rotate column x=40 by 1
rotate column x=33 by 2
rotate column x=32 by 3
rotate column x=31 by 2
rotate column x=28 by 1
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=25 by 1
rotate column x=23 by 5
rotate column x=22 by 5
rotate column x=21 by 5
rotate column x=18 by 5
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 5
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 1
rotate column x=2 by 5
rotate column x=1 by 5
rotate column x=0 by 1"""

class Screen(object):
	def __init__(self, width = 50, height = 6):
		self.width = width
		self.height = height
		self.matrix = [[' ' for x in range(self.width)] for y in range(self.height)]

	def rect(self, x, y):
		for row in xrange(0, y):
			for column in xrange(0, x):
				self.matrix[row][column] = '#'

	def read_column(self, column):
		columns = []
		for row in xrange(0, self.height):
			columns.append(self.matrix[row][column])
		return columns

	def read_row(self, row):
		rows = []
		for column in xrange(0, self.width):
			rows.append(self.matrix[row][column])
		return rows

	def rotate(self, command, argument, amount):
		if command == 'column':
			columns = self.read_column(argument)
			while amount >= self.height:
				amount -= self.height
			new_column = columns[self.height-amount:self.height] + columns[0:self.height-amount]
			for row in xrange(0, self.height):
				self.matrix[row][argument] = new_column[row]
		else:
			rows = self.read_row(argument)
			while amount >= self.width:
				amount -= self.width
			new_row = rows[self.width-amount:self.width] + rows[0:self.width-amount]
			for column in xrange(0, self.width):
				self.matrix[argument][column] = new_row[column]

	def display(self):
		for row in self.matrix:
			print row
		print '\n'

	def count_lit_pixels(self):
		counter = 0
		for rows in self.matrix:
			for column in rows:
				if column == '#':
					counter += 1
		return counter

def parser(line):
	m = re.search('^rect\s(?P<columns>[0-9]+)x(?P<rows>[0-9]+)', line)
	if m:
		display.rect(int(m.group('columns')), int(m.group('rows')))
	m = re.search('^rotate\s(?P<command>column|row)\s(x|y)=(?P<argument>[0-9]+)\sby\s(?P<amount>[0-9]+)', line)
	if m:
		display.rotate(m.group('command'), int(m.group('argument')), int(m.group('amount')))

lines = input.split('\n')

display = Screen(width=50, height=6)

for line in lines:
	parser(line)
	display.display()

print "Total lit pixels is: %d" % display.count_lit_pixels()
