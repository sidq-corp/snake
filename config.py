from termcolor import colored

colors = {1:'green',
		  2:'blue',
		  3:'cyan',
		  4:'magenta'}

sumbol_1 = '■'

weigth = 90
heigth = 22

start_h = heigth // 2
start_w = weigth // 2 

old_h = start_h
old_w = start_w

mode = 0

vector = 1

length = 10

markerh = 1

markerw = 1

kords = [[0, 0]]

stop = False

score = 0
matrix = [[sumbol_1 for i in range(weigth)] for i in range(heigth)]