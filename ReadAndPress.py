from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uinput

browser = webdriver.Firefox()
browser.get('http://www.twitch.tv/araujojordan')

teclas = (
	uinput.KEY_UP,
	uinput.KEY_DOWN,
	uinput.KEY_LEFT,
	uinput.KEY_RIGHT,
	uinput.KEY_A,
	uinput.KEY_B,
	uinput.KEY_X,
	uinput.KEY_Y,
	uinput.KEY_L,
	uinput.KEY_R,
	uinput.KEY_S, #select
	uinput.KEY_P #start
	)
device = uinput.Device(teclas)

while True:
	try:
		elements = browser.find_elements_by_class_name("chat_line")
		for elem in elements:

			comando = elem.get_attribute("innerHTML")
			if comando == 'up' or comando == 'UP' or comando == 'Up':
				device.emit_click(uinput.KEY_UP)
			elif comando == 'down' or comando == 'DOWN' or comando == 'Down':
				device.emit_click(uinput.KEY_DOWN)
			elif comando == 'right' or comando == 'RIGHT' or comando == 'Right':
				device.emit_click(uinput.KEY_RIGHT)
			elif comando == 'left' or comando == 'LEFT' or comando == 'Left':
				device.emit_click(uinput.KEY_LEFT)
			elif comando == 'b' or comando == 'B':
				device.emit_click(uinput.KEY_B)
			elif comando == 'start' or comando == 'Start' or comando == 'START':
				device.emit_click(uinput.KEY_P)
			elif comando == 'select' or comando == 'Select' or comando == 'SELECT':
				device.emit_click(uinput.KEY_S)
			elif comando == 'a' or comando == 'A':
				device.emit_click(uinput.KEY_A)
			elif comando == 'X' or comando == 'x':
				device.emit_click(uinput.KEY_X)
			elif comando == 'Y' or comando == 'y':
				device.emit_click(uinput.KEY_Y)
			elif comando == 'L' or comando == 'l':
				device.emit_click(uinput.KEY_L)
			elif comando == 'R' or comando == 'r':
				device.emit_click(uinput.KEY_R)

	except Exception: #Erro acontece quando um elemento eh deletado ou reaproveitado pelo codigo
		continue #melhor opcao econtrada eh ignorar para que ele passe para o proximo