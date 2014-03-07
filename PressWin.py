import time
import win32api # instalation files on dir: WinLibs/
import win32com.client

k = win32com.client.Dispatch("WScript.Shell")

def adjustText(text):
	return text.lower().replace(" ", "").replace(".","")
#	Hold the key for 0.5 seconds
def hold(char):
    k.SendKeys(char)
    #time.sleep(0.1)	doest work on win32api

#	Read and Press the comments list (SNES CONTROL)
def readAndPress(chat_list):
	for chat_line in chat_list:
		chat_line = adjustText(chat_line)
		if chat_line == 'up':
			hold("{UP}")
		elif chat_line == 'down':
			hold("{DOWN}")
		elif chat_line == 'right':
			hold("{RIGHT}")
		elif chat_line == 'left':
			hold("{LEFT}")
		elif chat_line == 'start':
			hold('p')
		elif chat_line == 'select':
			hold('s')
		elif chat_line == 'b':
			hold('b')
		elif chat_line == 'a':
			hold('a')
		elif chat_line == 'x':
			hold('x')
		elif chat_line == 'y':
			hold('y')
		elif chat_line == 'l':
			hold('l')
		elif chat_line == 'r':
			hold('r')
		else:
			return
		print chat_line
