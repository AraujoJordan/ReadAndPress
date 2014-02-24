from Press import *
from Read import *

def connect(url):
	
	browser = webdriver.Firefox()
	browser.get('http://www.twitch.tv/'+url)

	while True:
		
		try:
			item_list = browser.find_elements_by_class_name("chat_line")
		except Exception:
			pass

		press(read(item_list))

connect('araujojordan')