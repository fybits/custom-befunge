#!/usr/bin/python3

from random import choice 
from base64 import decodebytes

codeSize = 128
stack = []

RIGHT = (1,0)
DOWN = (0,1)
LEFT = (-1,0)
UP = (0, -1)

def pop():
	global stack
	if len(stack) == 0:
		return 0
	else:
		return stack.pop()

def push(char):
	global stack
	stack.append(char)


def run(code):
	# start
	currentCommand = (0,0)
	direction = (1,0)
	nextCommand = currentCommand
	ended = False
	string_mode = False

	while ended == False:
		# execute command
		c = code[currentCommand[0]][currentCommand[1]]
		if c == '"':
			string_mode = not string_mode
		elif string_mode == True:
			push(ord(c))
		elif c == ' ':
			pass
		elif c == '>':
			direction = RIGHT
		elif c == 'v':
			direction = DOWN
		elif c == '<':
			direction = LEFT
		elif c == '^':
			direction = UP
		elif c == '@':
			ended = True
		elif c in "0123456789":
			push(int(c))
		elif c == ':':
			temp = pop()
			push(temp)
			push(temp)
		elif c == '\\':
			a = pop()
			b = pop()
			push(a)
			push(b)
		elif c == '$':
			pop()
		elif c == '_':
			if pop() == 0:
				direction = RIGHT
			else:
				direction = LEFT
		elif c == '|':
			if pop() == 0:
				direction = DOWN
			else:
				direction = UP
		elif c == '?':
			direction = choice([RIGHT,DOWN,LEFT,UP])
		elif c == '+':
			push(pop()+pop())
		elif c == '-':
			sub = pop()
			push(pop()-sub)
		elif c == '*':
			push(pop()*pop())
		elif c == '/':
			delimiter = pop()
			push(int(pop()/delimiter))
		elif c == '%':
			delimiter = pop()
			push(pop()%delimiter)
		elif c == '!':
			if pop() == 0:
				push(1)
			else:
				push(0)
		elif c == '`':
			if pop() < pop():
				push(1)
			else:
				push(0)
		elif c == '&':
			try:
				push(int(input()))
			except ValueError  as err:
				print("Wrong value exception. Expected 'Integer'.")
				exit()
		elif c == '~':
			push(ord(input()))
		elif c == '.':
			print(pop(), end = '')
		elif c == ',':
			print(chr(pop()), end = '')
		elif c == 'p':
			y = pop()
			x = pop()
			code[x][y] = chr(pop())
		elif c == 'g':
			y = pop()
			x = pop()
			push(code[x][y])
		
		nextCommand = [ sum(x)%codeSize for x in zip(currentCommand,direction)]
		if c == '#':
			nextCommand = [ sum(x)%codeSize for x in zip(nextCommand,direction)]
		elif c == 'j':
			nextCommand = (pop(), pop())
		#print(stack)

		currentCommand = nextCommand
