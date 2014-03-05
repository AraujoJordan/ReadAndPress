from pykeyboard import PyKeyboard #need Xlib
import time

k = PyKeyboard()

#	Hold the key for 0.5 seconds
def hold(character):
    k.press_key(character)
    time.sleep(0.5)
    k.release_key(character)	

#	Read and Press the comments list (SNES CONTROL)
def readAndPress(chat_list):
	for chat_line in chat_list:
		if chat_line == 'up' or chat_line == 'UP' or chat_line == 'Up':
			hold(k.up_key)
		elif chat_line == 'down' or chat_line == 'DOWN' or chat_line == 'Down':
			hold(k.down_key)
		elif chat_line == 'right' or chat_line == 'RIGHT' or chat_line == 'Right':
			hold(k.right_key)
		elif chat_line == 'left' or chat_line == 'LEFT' or chat_line == 'Left':
			hold(k.left_key)
		elif chat_line == 'start' or chat_line == 'Start' or chat_line == 'START':
			k.type_string('p')
		elif chat_line == 'select' or chat_line == 'Select' or chat_line == 'SELECT':
			k.type_string('s')
		elif chat_line == 'b' or chat_line == 'B':
			k.type_string('b')
		elif chat_line == 'a' or chat_line == 'A':
			k.type_string('a')
		elif chat_line == 'X' or chat_line == 'x':
			k.type_string('x')
		elif chat_line == 'Y' or chat_line == 'y':
			k.type_string('y')
		elif chat_line == 'L' or chat_line == 'l':
			k.type_string('l')
		elif chat_line == 'R' or chat_line == 'r':
			k.type_string('r')
		else:
			return
		print chat_line