import random


class Wall():
    def __init__(self):
        self.symbol = "#"

    def fabricate(self, Board):

        for i in range(Board._length):
            for j in range(Board._breadth):
                if (i %
                    8 == 0 and j %
                    4 == 0) or (i %
                                8 == 1 and j %
                                4 == 0) or (i %
                                            8 == 2 and j %
                                            4 == 0) or (i %
                                                        8 == 3 and j %
                                                        4 == 0):
                    Board._board[i][j] = self.symbol
                if (i %
                    8 == 0 and j %
                    4 == 1) or (i %
                                8 == 1 and j %
                                4 == 1) or (i %
                                            8 == 2 and j %
                                            4 == 1) or (i %
                                                        8 == 3 and j %
                                                        4 == 1):
                    Board._board[i][j] = self.symbol


class Brick(Wall):
    """docstring for Brick"""

    def __init__(self):
        super(Brick, self).__init__()
        self.symbol = "/"

    def fabricate(self, Board, wall):

        overlap = 1
        while (overlap):
            self._position_x = random.randrange(12, Board._length - 4, 4)
            self._position_y = random.randrange(6, Board._breadth - 3, 2)
            if (Board._board[self._position_x][self._position_y] !=
                    wall.symbol and Board._board[self._position_x][self._position_y] != self.symbol):
                overlap = 0
        for i in range(self._position_x, self._position_x + 4):
            for j in range(self._position_y, self._position_y + 2):
                Board._board[i][j] = self.symbol
