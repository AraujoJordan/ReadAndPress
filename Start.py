import sys

if sys.platform == 'win32':
  from PressWin import *
elif 'linux' in sys.platform:
  from PressLinux import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread

URL = 'http://www.twitch.tv/twitchplayspokemon' #you can use www.justin.tv too
oldListSize = 0

#	This method check if the chat list is >= 1 element
#	then, read all coments in a new thread.
def readAndClear(chat_list,browser):
	global oldListSize

	if len(chat_list) > oldListSize:
		textList = []
		while len(chat_list) > oldListSize:
			textList.append(chat_list[oldListSize].text) #add a text line of chat on a list
			oldListSize = oldListSize+1

		thread = Thread(target = readAndPress, args = (textList,))
		thread.start()

		if len(chat_list) >=150:
			browser.execute_script('CurrentChat.clear_chat_lines()') #clear the browser chat
			listSize = 0

#	Call the browser Firefox and read the coments in the chat of Twitch/Justin
def connect(url):
	browser = webdriver.Firefox()
	browser.get(url)

	#loop until the CTRL+C (to stop the program)
	while True:		
		try:
			chat_list = browser.find_elements_by_class_name("chat_line")
		except Exception:
			readAndClear(chat_list,browser)
			continue
		readAndClear(chat_list,browser)

#begin
connect(URL)
