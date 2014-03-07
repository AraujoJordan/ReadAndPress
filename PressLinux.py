from pykeyboard import PyKeyboard #need Xlib
import time

k = PyKeyboard()

def adjustText(text):
	return text.lower().replace(" ", "").replace(".","")

#	Hold the key for 0.5 seconds
def hold(character):
    k.press_key(character)
    time.sleep(0.5)
    k.release_key(character)	

#	Read and Press the comments list (SNES CONTROL)
def readAndPress(chat_list):
	for chat_line in chat_list:
		chat_line = adjustText(chat_line)
		if chat_line == 'up':
			hold(k.up_key)
		elif chat_line == 'down':
			hold(k.down_key)
		elif chat_line == 'right':
			hold(k.right_key)
		elif chat_line == 'left':
			hold(k.left_key)
		elif chat_line == 'start':
			k.type_string('p')
		elif chat_line == 'select':
			k.type_string('s')
		elif chat_line == 'b':
			k.type_string('b')
		elif chat_line == 'a':
			k.type_string('a')
		elif chat_line == 'x':
			k.type_string('x')
		elif chat_line == 'y':
			k.type_string('y')
		elif chat_line == 'l':
			k.type_string('l')
		elif chat_line == 'r':
			k.type_string('r')
		else:
			return
		print chat_line