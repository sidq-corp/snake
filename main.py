import os 
import time
import keyboard
from termcolor import colored
import threading
import config as c
from random import randint
# def print_pressed_keys(e):
#     print(e.name)


# keyboard.hook(print_pressed_keys)
# keyboard.wait()

def cheker():
	if [c.start_h, c.start_w] in c.kords or c.start_h < 0 or c.start_h > c.heigth - 1 or c.start_w > c.weigth - 1 or c.start_w < 0:
		c.stop = False
		time.sleep(0.4)
		os.system('cls')
		print(colored('Score: ' + str(c.score), 'red'))
		quit()

def new_marker():
	c.markerh = randint(3,c.heigth - 3)
	c.markerw = randint(3,c.weigth - 3)
	c.matrix[c.markerh][c.markerw] = colored(c.sumbol_1, 'yellow')

new_marker()

def matrix_hendler():
	if c.start_w == c.markerw and c.start_h == c.markerh:
		new_marker()
		c.length += 2
		c.score += 1
	cheker()
	c.kords.append([c.start_h, c.start_w])
	if len(c.kords) > c.length:
		q = len(c.kords) - c.length
		c.matrix[c.kords[q][0]][c.kords[q][1]] = c.sumbol_1
		del c.kords[q]
	os.system('cls')
	c.matrix[c.old_h][c.old_w] = colored(c.sumbol_1, c.colors[randint(1,4)])
	c.matrix[c.start_h][c.start_w] = colored(c.sumbol_1, 'red')
	c.old_h = c.start_h
	c.old_w = c.start_w
	for i in range(c.heigth):
		print(''.join(c.matrix[i]))

matrix_hendler() 


# def pall():
# 	c.matrix = [[c.sumbol_1 for i in range(c.weigth)] for i in range(c.heigth)]
# 	matrix_hendler()

def up():
	c.start_h-=1
	if c.start_h < 0:
		c.start_h = 1
	matrix_hendler()	

def down():
	c.start_h+=1
	if c.start_h > c.heigth - 1:
		c.start_h = c.heigth - 1
	matrix_hendler()

def right():
	c.start_w+=1
	if c.start_w > c.weigth - 1:
		c.start_w = c.weigth - 1
	matrix_hendler()

def left():
	c.start_w-=1
	if c.start_w < 0:
		c.start_w = 0
	matrix_hendler()

# def mode():
# 	c.mode = 0 if c.mode else 1
# 	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2

def ups():
	c.vector = 2
def lefts():
	c.vector = 1
def downs():
	c.vector = 4
def rights():
	c.vector = 3

def main():
	while c.stop:
		if c.vector == 1:
			left()
		elif c.vector == 2:
			up()
		elif c.vector == 3:
			right()
		elif c.vector == 4:
			down()
		time.sleep(0.3)

def init():
	if not c.stop:
		c.stop = True
		thr = threading.Thread(target=main)
		thr.start()

keyboard.add_hotkey('c', init)
# keyboard.add_hotkey('n', pall)
keyboard.add_hotkey('up', ups)
keyboard.add_hotkey('down', downs)
keyboard.add_hotkey('right', rights)
keyboard.add_hotkey('left', lefts)
# keyboard.add_hotkey('m', mode)
keyboard.wait('Esc')

