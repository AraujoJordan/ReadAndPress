from selenium import webdriver
from selenium.webdriver.common.keys import Keys

lastElemID = 'nothing'
elemLenElement = 'nothing'

def read(item_list):
	global lastElemID
	global lastElemLen

	if item_list:
		item = item_list[-1]
		if item.id == lastElemID: #and item.get_attribute('len()')<=lastElemLen:
			return None
		lastElemID = item.id
		#lastElemLen = item.get_attribute('len()')
		return item.text

	return None