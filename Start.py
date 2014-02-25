from ReadAndPress import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread

URL = 'http://www.twitch.tv/twitchplayspokemon' #you can use www.justin.tv too

#	This method check if the chat list is >= 1 element
#	then, read all coments in a new thread.
def readAndClear(chat_list,browser):
	chat_text_list = []
	if len(chat_list)>=1:
		for chat_element in chat_list:
			chat_text_list.append(chat_element.text) #get only the text
		thread = Thread(target = readAndPress, args = (list(chat_text_list),)) #run a thread for readAndPress
		del chat_text_list[:] #clear list
		thread.start()
		browser.execute_script('CurrentChat.clear_chat_lines()') #clear the browser chat

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