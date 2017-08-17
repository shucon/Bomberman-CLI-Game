from random import randint
import signal,time
from board import *
from player import *
from obstacle import *
def main():
	villan_cnt = 5
	villan = []
	hero = Hero()
	board_obj = Board()
	wall = Wall()
	wall.fabricate(board_obj)
	brick = []
	brick_cnt = 16
	for i in range(brick_cnt):
		brick.append(Brick())
		brick[i].fabricate(board_obj,wall)
	for i in range (villan_cnt):
		villan.append(Villan(board_obj,brick,wall))
		board_obj.playerDraw(villan[i])
	board_obj.playerDraw(hero)
	board_obj.draw()
	print("Score: " , hero._score , "  Lives: " , hero._lives , "  Level: 1")
if __name__ == '__main__':
	main()