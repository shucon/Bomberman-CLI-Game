import random


class Hero():
    """docstring for Hero"""

    def __init__(self):
        self.position_x = 4
        self.position_y = 2
        self.uppershape = ["[", "^", "^", "]"]
        self.lowershape = [" ", "]", "[", " "]
        self.lives = 3
        self.score = 0

    def clr(self, Board):
        for i in range(4):
            Board.board[self.position_x + i][self.position_y] = " "
        for i in range(4):
            Board.board[self.position_x + i][self.position_y + 1] = " "

    def kill(self, board):
        self.clr(board)
        self.lives -= 1
        self.position_x = 4
        self.position_y = 2


class Villan(Hero):
    """docstring for Villan"""

    def __init__(self, board, brick, wall):
        super(Villan, self).__init__()
        overlap = 1
        while (overlap):
            self.position_x = random.randrange(16, board.length - 4, 4)
            self.position_y = random.randrange(10, board.breadth - 3, 2)
            if board.board[self.position_x][self.position_y] == board.freesymbol:
                overlap = 0
        self.uppershape = ["^", "O", "O", "^"]
        self.lowershape = [" ", "}", "{", " "]
        self.status = 1  # 1 -> Life   0 -> Death

    def kill(self, board, hero):
        hero.score += 100
        self.status = 0
        self.clr(board)

    def motion(self, board, bomb, hero):
        # 0 -> UP 1-> DOWN 2 -> LEFT 3 -> RIGHT
        if self.status == 0:
            return
        overlap = 1
        motion = random.randrange(0, 4)
        count = 0
        while (overlap):
            if motion == 0:
                check_y = self.position_y - 2
                check_x = self.position_x
            if motion == 1:
                check_y = self.position_y + 2
                check_x = self.position_x
            if motion == 2:
                check_y = self.position_y
                check_x = self.position_x - 4
            if motion == 3:
                check_y = self.position_y
                check_x = self.position_x + 4
            if board.board[check_x][check_y] == board.freesymbol or board.board[check_x][check_y] == "[":
                overlap = 0
                self.clr(board)
                self.position_x = check_x
                self.position_y = check_y
                if self.position_x == hero.position_x and self.position_y == hero.position_y:
                    hero.kill(board)
            motion = (motion + 1) % 4
            count += 4
            if count > 5:
                break

        board.playerDraw(self)
