import time
import win32api # instalation files on dir: WinLibs/
import win32com.client

k = win32com.client.Dispatch("WScript.Shell")

#	Hold the key for 0.5 seconds
def hold(char):
    shell.SendKeys(char)
    time.sleep(0.1)	

#	Read and Press the comments list (SNES CONTROL)
def readAndPress(chat_list):
	for chat_line in chat_list:
		if chat_line.lower() == 'up':
			hold("{UP}")
		elif chat_line.lower() == 'down':
			hold(k.down_key)
		elif chat_line.lower() == 'right':
			hold(k.right_key)
		elif chat_line.lower() == 'left':
			hold(k.left_key)
		else:
			return
		print chat_line
