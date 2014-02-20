from selenium import webdriver
import uinput
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.twitch.tv/twitchplayspokemon')

device = uinput.Device([uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_A, uinput.KEY_B, uinput.KEY_S, uinput.KEY_P])

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
			elif comando == 'a' or comando == 'A':
				device.emit_click(uinput.KEY_A)
			elif comando == 'b' or comando == 'B':
				device.emit_click(uinput.Key_B)
			elif comando == 'start' or comando == 'Start' or comando == 'START':
				device.emit_click(uinput.Key_P)
			elif comando == 'select' or comando == 'Select':
				device.emit_click(uinput.Key_S)

	except Exception: #Erro acontece por elemento deletado ou reaproveitado pelo código
		print comando #melhor opção acredito que é ignorar para que ele passe pro proximo