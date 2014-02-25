from selenium import webdriver
from selenium.webdriver.common.keys import Keys

lastElemID = 'nothing'
elemLenElement = 'nothing'

def read(item_list):
	global lastElemID
	global listLen

	if item_list:
		item = item_list[-1]
		if item.id == lastElemID and len(item_list)<=listLen:
			return None
		lastElemID = item.id
		listLen = len(item_list)
		return item.text

	return None