from random import randrange
from obstacle import *
from termcolor import colored


class Board():
    """Manage and print game"""

    def __init__(self):
        self.breadth = 34
        self.length = 76
        self.board = []
        self.freesymbol = " "
        for i in range(self.length):
            self.board.append([])
            for j in range(self.breadth):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == self.length - \
                        3 or i == self.length - 4 or i == self.length - 2 or i == self.length - 1:
                    self.board[i].append("#")
                else:
                    if j == 0 or j == 1 or j == self.breadth - 2 or j == self.breadth - 1:
                        self.board[i].append("#")
                    else:
                        self.board[i].append(self.freesymbol)

    def draw(self):
        for j in range(self.breadth):
            print()
            for i in range(self.length):
                if self.board[i][j] == "/":
                    print(
                        colored(
                            self.board[i][j],
                            'yellow',
                            attrs=['bold']),
                        end='')
                elif self.board[i][j] == "[" or self.board[i][j] == "]" or self.board[i][j] == "^":
                    print(
                        colored(
                            self.board[i][j],
                            'cyan',
                            attrs=['bold']),
                        end='')
                elif self.board[i][j] == "O" or self.board[i][j] == "}" or self.board[i][j] == "{":
                    print(
                        colored(
                            self.board[i][j],
                            'magenta',
                            attrs=['bold']),
                        end='')
                elif self.board[i][j] == "0" or self.board[i][j] == "1" or self.board[i][j] == "2" or self.board[i][j] == "3" or self.board[i][j] == "|":
                    print(
                        colored(
                            self.board[i][j],
                            'red',
                            attrs=['bold']),
                        end='')
                else:
                    print(self.board[i][j], end='')
        print()

    def random_wall(self):
        x = random.randrange(2, self.length - 3)
        y = random.randrange(2, self.breadth - 3)

    def playerDraw(self, player):
        for i in range(4):
            self.board[player.position_x +
                        i][player.position_y] = player.uppershape[i]
        for i in range(4):
            self.board[player.position_x +
                        i][player.position_y +
                           1] = player.lowershape[i]

    def bombDraw(self, player, bomb, vill):
        if bomb.position_x != -1 and (player.position_x != bomb.position_x or player.position_y != bomb.position_y) and self.board[bomb.position_x][bomb.position_y] != vill[0].uppershape[0]:
            for i in range(4):
                self.board[bomb.position_x +
                            i][bomb.position_y] = bomb.uppershape[i]
                self.board[bomb.position_x +
                            i][bomb.position_y +
                               1] = bomb.lowershape[i]

        if bomb.position_x == -1:
            for i in range(4):
                self.board[bomb.prev_x + i][bomb.prev_y] = self.freesymbol
                self.board[bomb.prev_x +
                            i][bomb.prev_y + 1] = self.freesymbol

            # Restore blast shape
            for i in range(bomb.prev_x - 4, bomb.prev_x + 8):
                if self.board[i][bomb.prev_y] != "#":
                    self.board[i][bomb.prev_y] = self.freesymbol
                    self.board[i][bomb.prev_y + 1] = self.freesymbol

            for i in range(bomb.prev_x, bomb.prev_x + 4):
                if self.board[i][bomb.prev_y - 2] != "#":
                    self.board[i][bomb.prev_y - 2] = self.freesymbol
                    self.board[i][bomb.prev_y - 1] = self.freesymbol
                if self.board[i][bomb.prev_y + 2] != "#":
                    self.board[i][bomb.prev_y + 2] = self.freesymbol
                    self.board[i][bomb.prev_y + 3] = self.freesymbol

            bomb.prev_x = -1
            bomb.prev_y = -1
