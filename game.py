import random
import signal,copy,sys,time
from board import *
from player import *
from obstacle import *
from getchunix import *
from alarmexception import *
from controls import *
from bomb import *

getch = GetchUnix()	

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print(end='')
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def main():
	print("Press any key to start game")
	villan_cnt = 2
	villan = []
	hero = Hero()
	board_obj = Board()
	wall = Wall()
	wall.fabricate(board_obj)
	brick = []
	bomb = Bomb()
	brick_cnt = 35
	for i in range(brick_cnt):
		brick.append(Brick())
		brick[i].fabricate(board_obj,wall)
	for i in range (villan_cnt):
		villan.append(Villan(board_obj,brick,wall))
	
	while(hero._lives):
		
		move = input_to()
		controls(move,hero,board_obj,bomb)
		for i in range (villan_cnt):
			villan[i].motion(board_obj,bomb,hero)
		board_obj.bombDraw(hero,bomb,villan)
		if(bomb._positionX != -1):
			bomb._time -= 1
			bomb._upperShape=[bomb._boundary,bomb._time,bomb._time,bomb._boundary]
			bomb._lowerShape=[bomb._boundary,bomb._time,bomb._time,bomb._boundary]
		if(bomb._time == -1):
			bomb.blast(board_obj,hero,villan,villan_cnt)
			blast = 1
		board_obj.playerDraw(hero)
		board_obj.draw()
		print("Score: " , hero._score , "  Lives: " , hero._lives , "  Level: 1")
if __name__ == '__main__':
	main()