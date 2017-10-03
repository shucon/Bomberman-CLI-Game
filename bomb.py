'''Time Module'''
import time


class Bomb():
    def __init__(self, level):
        self.position_x = -1
        self.position_y = -1
        self.prev_x = -1
        self.prev_y = -1
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

    def plant(self, hero):
        if self.position_x == -1:
            self.position_x = hero.position_x
            self.position_y = hero.position_y

    def blast(self, board, hero, villan):
        self.blastshape = "^"
        self.prev_x = self.position_x
        self.prev_y = self.position_y
        self.position_x = -1
        self.position_y = -1
        self.time = 4

        # Brick score

        if board.board[self.prev_x - 4][self.prev_y] == "/":
            hero.score += 20

        if board.board[self.prev_x + 4][self.prev_y] == "/":
            hero.score += 20

        if board.board[self.prev_x][self.prev_y - 2] == "/":
            hero.score += 20

        if board.board[self.prev_x][self.prev_y + 2] == "/":
            hero.score += 20

        for i in range(self.prev_x - 4, self.prev_x + 8):
            if board.board[i][self.prev_y] != "#":
                board.board[i][self.prev_y] = self.blastshape
                board.board[i][self.prev_y + 1] = self.blastshape

        for i in range(self.prev_x, self.prev_x + 4):
            if board.board[i][self.prev_y - 2] != "#":
                board.board[i][self.prev_y - 2] = self.blastshape
                board.board[i][self.prev_y - 1] = self.blastshape

            if board.board[i][self.prev_y + 2] != "#":
                board.board[i][self.prev_y + 2] = self.blastshape
                board.board[i][self.prev_y + 3] = self.blastshape
        if (hero.position_x >= self.prev_x - 4 and hero.position_x < self.prev_x + 5) and (hero.position_y == self.prev_y) or ((hero.position_y >= self.prev_y - 2 and hero.position_y < self.prev_y + 3) and hero.position_x == self.prev_x):
            hero.kill(board)

        for i in range(self.villan_cnt):
            if (villan[i].position_x >= self.prev_x - 4 and villan[i].position_x < self.prev_x + 5) and (villan[i].position_y == self.prev_y) or ((villan[i].position_y >= self.prev_y - 2 and villan[i].position_y < self.prev_y + 3) and villan[i].position_x == self.prev_x):
                self.villan_cnt -= 1
                villan[i].kill(board, hero)
