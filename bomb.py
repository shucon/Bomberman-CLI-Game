class Bomb():
	def __init__(self):
		self._upperShape=["|","B","B","|"]
		self._lowerShape=["|","B","B","|"]

	def plant(self,hero,board):
		for i in range(4):
			board._board[hero._positionX+i][hero._positionY] = self._upperShape[i]
		for i in range(4):
			board._board[hero._positionX+i][hero._positionY+1] = self._lowerShape[i]

