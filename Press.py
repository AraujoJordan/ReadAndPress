from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

def press_and_hold(character):
    k.press_key(character)
    time.sleep(0.5)
    k.release_key(character)

def press(cmd):
	if None:
		return None
	if cmd == 'up' or cmd == 'UP' or cmd == 'Up':
		print cmd
		press_and_hold(k.up_key)
	elif cmd == 'down' or cmd == 'DOWN' or cmd == 'Down':
		print cmd
		press_and_hold(k.down_key)
	elif cmd == 'right' or cmd == 'RIGHT' or cmd == 'Right':
		print cmd
		press_and_hold(k.right_key)
	elif cmd == 'left' or cmd == 'LEFT' or cmd == 'Left':
		print cmd
		press_and_hold(k.left_key)
	elif cmd == 'start' or cmd == 'Start' or cmd == 'START':
		print cmd
		k.type_string('p')
	elif cmd == 'select' or cmd == 'Select' or cmd == 'SELECT':
		print cmd
		k.type_string('s')
	elif cmd == 'b' or cmd == 'B':
		print cmd
		k.type_string('b')
	elif cmd == 'a' or cmd == 'A':
		print cmd
		k.type_string('a')
	elif cmd == 'X' or cmd == 'x':
		print cmd
		k.type_string('x')
	elif cmd == 'Y' or cmd == 'y':
		print cmd
		k.type_string('y')
	elif cmd == 'L' or cmd == 'l':
		print cmd
		k.type_string('l')
	elif cmd == 'R' or cmd == 'r':
		print cmd
		k.type_string('r')