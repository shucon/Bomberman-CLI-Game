from random import randint
import signal,copy,sys,time
from board import *
from player import *
from obstacle import *
from getchunix import *
from alarmexception import *
from controls import *

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
	
	while(hero._lives and villan_cnt):
		
		move = input_to()
		controls(move,hero,board_obj)
		for i in range (villan_cnt):
			villan[i].motion(board_obj)
		board_obj.playerDraw(hero)
		board_obj.draw()
		print("Score: " , hero._score , "  Lives: " , hero._lives , "  Level: 1")
if __name__ == '__main__':
	main()