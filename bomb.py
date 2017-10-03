import time


class Bomb():
    def __init__(self, level):
        self.position_x = -1
        self.position_y = -1
        self.prevX = -1
        self.prevY = -1
        self.time = 4
        self.boundary = "|"
        self.uppershape = [
            self.boundary,
            self.time,
            self.time,
            self.boundary]
        self.lowershape = [
            self.boundary,
            self.time,
            self.time,
            self.boundary]
        self.villan_cnt = 3 * level
        self.plant_time = time.time()

    def plant(self, hero, board):
        if(self.position_x == -1):
            self.position_x = hero.position_x
            self.position_y = hero.position_y

    def blast(self, board, hero, villan):
        self.blastshape = "^"
        self.prevX = self.position_x
        self.prevY = self.position_y
        self.position_x = -1
        self.position_y = -1
        self.time = 4

        # Brick score

        if board.board[self.prevX - 4][self.prevY] == "/":
            hero.score += 20

        if board.board[self.prevX + 4][self.prevY] == "/":
            hero.score += 20

        if board.board[self.prevX][self.prevY - 2] == "/":
            hero.score += 20

        if board.board[self.prevX][self.prevY + 2] == "/":
            hero.score += 20

        for i in range(self.prevX - 4, self.prevX + 8):
            if(board.board[i][self.prevY] != "#"):
                board.board[i][self.prevY] = self.blastshape
                board.board[i][self.prevY + 1] = self.blastshape

        for i in range(self.prevX, self.prevX + 4):
            if(board.board[i][self.prevY - 2] != "#"):
                board.board[i][self.prevY - 2] = self.blastshape
                board.board[i][self.prevY - 1] = self.blastshape

            if(board.board[i][self.prevY + 2] != "#"):
                board.board[i][self.prevY + 2] = self.blastshape
                board.board[i][self.prevY + 3] = self.blastshape
        if(((hero.position_x >= self.prevX - 4 and hero.position_x < self.prevX + 5) and (hero.position_y == self.prevY)) or ((hero.position_y >= self.prevY - 2 and hero.position_y < self.prevY + 3) and hero.position_x == self.prevX)):
            hero.kill(board)

        for i in range(self.villan_cnt):
            if(((villan[i].position_x >= self.prevX - 4 and villan[i].position_x < self.prevX + 5) and (villan[i].position_y == self.prevY)) or ((villan[i].position_y >= self.prevY - 2 and villan[i].position_y < self.prevY + 3) and villan[i].position_x == self.prevX)):
                self.villan_cnt -= 1
                villan[i].kill(board, hero)
