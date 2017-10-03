import random


class Hero():
    """docstring for Hero"""

    def __init__(self):
        self._position_x = 4
        self._position_y = 2
        self._uppershape = ["[", "^", "^", "]"]
        self._lowershape = [" ", "]", "[", " "]
        self._lives = 3
        self._score = 0

    def clr(self, Board):
        for i in range(4):
            Board._board[self._position_x + i][self._position_y] = " "
        for i in range(4):
            Board._board[self._position_x + i][self._position_y + 1] = " "

    def kill(self, board):
        self.clr(board)
        self._lives -= 1
        self._position_x = 4
        self._position_y = 2


class Villan(Hero):
    """docstring for Villan"""

    def __init__(self, board, brick, wall):
        super(Villan, self).__init__()
        overlap = 1
        while (overlap):
            self._position_x = random.randrange(16, board._length - 4, 4)
            self._position_y = random.randrange(10, board._breadth - 3, 2)
            if (board._board[self._position_x]
                    [self._position_y] == board._freesymbol):
                overlap = 0
        self._uppershape = ["^", "O", "O", "^"]
        self._lowershape = [" ", "}", "{", " "]
        self._status = 1  # 1 -> Life   0 -> Death

    def kill(self, board, hero):
        hero._score += 100
        self._status = 0
        self.clr(board)

    def motion(self, board, bomb, hero):
        # 0 -> UP 1-> DOWN 2 -> LEFT 3 -> RIGHT
        if self._status == 0:
            return
        overlap = 1
        motion = random.randrange(0, 4)
        count = 0
        while (overlap):
            if(motion == 0):
                check_y = self._position_y - 2
                check_x = self._position_x
            if(motion == 1):
                check_y = self._position_y + 2
                check_x = self._position_x
            if(motion == 2):
                check_y = self._position_y
                check_x = self._position_x - 4
            if(motion == 3):
                check_y = self._position_y
                check_x = self._position_x + 4
            if (board._board[check_x][check_y] ==
                    board._freesymbol or board._board[check_x][check_y] == "["):
                overlap = 0
                self.clr(board)
                self._position_x = check_x
                self._position_y = check_y
                if(self._position_x == hero._position_x and self._position_y == hero._position_y):
                    hero.kill(board)
            motion = (motion + 1) % 4
            count += 4
            if (count > 5):
                break

        board.playerDraw(self)
