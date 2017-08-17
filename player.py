import random
class Hero():
	"""docstring for Hero"""
	def __init__(self):
		self._positionX = 4
		self._positionY = 2
		self._upperShape = ["[","^","^","]"]
		self._lowerShape = [" ","]","["," "]
		self._lives = 3
		self._score = 0

	def kill(self):
		self._lives -= 1
		self._positionX = 4
		self._positionY = 2

class Villan(Hero):
	"""docstring for Villan"""
	def __init__(self,board,brick,wall):
		super(Villan, self).__init__()
		overlap = 1
		while (overlap):
			self._positionX =random.randrange(16,board._length-4,4)
			self._positionY =random.randrange(10,board._breadth-3,2)
			if (board._board[self._positionX][self._positionY] != wall.symbol and board._board[self._positionX][self._positionY] != brick[0].symbol):
				overlap = 0
		self._upperShape = ["^","O","O","^"]
		self._lowerShape = [" ","]","["," "]

	def kill(self):
		self._score += 100
		