import random


class Wall():
    def __init__(self):
        self.symbol = "#"

    def fabricate(self, Board):

        for i in range(Board.length):
            for j in range(Board.breadth):
                if (i %
                    8 == 0 and j %
                    4 == 0) or (i %
                                8 == 1 and j %
                                4 == 0) or (i %
                                            8 == 2 and j %
                                            4 == 0) or (i %
                                                        8 == 3 and j %
                                                        4 == 0):
                    Board.board[i][j] = self.symbol
                if (i %
                    8 == 0 and j %
                    4 == 1) or (i %
                                8 == 1 and j %
                                4 == 1) or (i %
                                            8 == 2 and j %
                                            4 == 1) or (i %
                                                        8 == 3 and j %
                                                        4 == 1):
                    Board.board[i][j] = self.symbol


class Brick(Wall):
    """docstring for Brick"""

    def __init__(self):
        super(Brick, self).__init__()
        self.symbol = "/"

    def fabricate(self, Board, wall):

        overlap = 1
        while overlap:
            self.position_x = random.randrange(12, Board.length - 4, 4)
            self.position_y = random.randrange(6, Board.breadth - 3, 2)
            if Board.board[self.position_x][self.position_y] != wall.symbol and Board.board[self.position_x][self.position_y] != self.symbol:
                overlap = 0
        for i in range(self.position_x, self.position_x + 4):
            for j in range(self.position_y, self.position_y + 2):
                Board.board[i][j] = self.symbol
