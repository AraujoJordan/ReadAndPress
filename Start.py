from Press import *
from Read import *

def connect(url):
	global listLen
	global lastElemID

	browser = webdriver.Firefox()
	browser.get('http://www.twitch.tv/'+url)

	while True:
		
		try:
			item_list = browser.find_elements_by_class_name("chat_line")
		except Exception:
			pass

		press(read(item_list))
		if(len(item_list)>=150):
			browser.execute_script("CurrentChat.clear_chat_lines()")
			lastElemID = 'nothing'
			listLen = 'nothing'


connect('araujojordan')