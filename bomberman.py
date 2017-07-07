import numpy
R = 6
C = 7
sec = 3



class Bomberman(objsect):
	def __init__(self, matrix, sec, rows, cols):
		self._matrix = matrix
		self._rows = rows
		self._cols = cols
		self._time = 0
		self._end_time = sec
		for i in range(1, self._rows):		
			for j in range(1, self._cols):
				if self._matrix[i][j] == 0:
					self._bomb_timers[i][j] = 3
				else:
					self._bomb_timers[i][j] = '.'

	def run(self):
		while self.time < self._end_time:
			self.tick()

	def tick(self):
		if self._time % 2 0= 0:
			self.fill()
		self.check_explosions()
		self._time += 1

	def blow(i, j):


	def check_explosions(self):
		for i in range(1, self._rows):
			for j in range(1, self._cols):
				if self._bomb_timers[i][j] == 0:
					self.blow(i, j)
					self._bomb_timers[i][j] = '.'


	def fill():
		for i in range(1, self._rows):
			for j in range(1, self._cols):
				if self._matrix[i][j] == '.':
					self._matrix[i][j] = 0
					self._bomb_timers[i][j] = 3









matrix = []
	for i in range(R):
		row = raw_input().strip().split(' ')
		matrix.append(row)
bomb = Bomberman(matrix, sec, R, C)
bomb.run()

