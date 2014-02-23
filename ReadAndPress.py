#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uinput

elemAnterior = 'nenhum texto'
browser = webdriver.Firefox()
browser.get('http://www.twitch.tv/araujojordan')

teclas = (
	uinput.KEY_UP,
	uinput.KEY_DOWN,
	uinput.KEY_LEFT,
	uinput.KEY_RIGHT,
	uinput.KEY_A,
	uinput.KEY_B,
	#uinput.KEY_X,
	#uinput.KEY_Y,
	uinput.KEY_L,
	uinput.KEY_R,
	uinput.KEY_SPACE,
	uinput.KEY_ENTER
	)
device = uinput.Device(teclas)
device.emit(uinput.KEY_)

def get_Last(iterable):
	global elemAnterior
	if iterable:
		item = iterable[-1]
		if item.id == elemAnterior:
			return None
		txt = item.get_attribute("innerHTML")
		elemAnterior = item.id
		return txt
	return None

while True:
	try:
		elements = browser.find_elements_by_class_name("chat_line")
	except Exception: #Erro acontece quando um elemento eh deletado ou reaproveitado pelo codigo
		continue #melhor opcao econtrada eh ignorar para que ele passe para o proximo
		
	comando = get_Last(elements)
	if comando == '':
		continue
	#for elem in elements:
	if comando == 'up' or comando == 'UP' or comando == 'Up':
		device.emit_click(uinput.KEY_UP)
	elif comando == 'down' or comando == 'DOWN' or comando == 'Down':
		device.emit_click(uinput.KEY_DOWN)
	elif comando == 'right' or comando == 'RIGHT' or comando == 'Right':
		device.emit_click(uinput.KEY_RIGHT)
	elif comando == 'left' or comando == 'LEFT' or comando == 'Left':
		device.emit_click(uinput.KEY_LEFT)
	elif comando == 'b' or comando == 'B':
		device.emit_click(uinput.KEY_X)
	elif comando == 'start' or comando == 'Start' or comando == 'START':
		device.emit_click(uinput.KEY_ENTER)
	elif comando == 'select' or comando == 'Select' or comando == 'SELECT':
		device.emit_click(uinput.KEY_SPACE)
	elif comando == 'a' or comando == 'A':
		device.emit_click(uinput.KEY_Z)
	#elif comando == 'X' or comando == 'x':
	#	device.emit_click(uinput.KEY_X)
	#elif comando == 'Y' or comando == 'y':
	#	device.emit_click(uinput.KEY_Y)
	elif comando == 'L' or comando == 'l':
		device.emit_click(uinput.KEY_A)
	elif comando == 'R' or comando == 'r':
		device.emit_click(uinput.KEY_S)
