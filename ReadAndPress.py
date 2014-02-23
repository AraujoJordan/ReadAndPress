#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
import time

elemAnterior = 'nada'
txtAnterior = 'nada'
browser = webdriver.Firefox()
browser.get('http://www.twitch.tv/araujojordan')
#twitchplayspokemon

k = PyKeyboard()

def press_and_hold(character):
    k.press_key(character)
    time.sleep(0.5)
    k.release_key(character)

def get_Last(iterable):
	global elemAnterior
	global txtAnterior
	if iterable:
		item = iterable[-1]
		if item.id == elemAnterior and item.text==txtAnterior:
			return None
		elemAnterior = item.id
		txtAnterior = item.text
		return item.text
	return None

while True:
	try:
		elements = browser.find_elements_by_class_name("chat_line")
	except Exception: #Erro acontece quando um elemento eh deletado ou reaproveitado pelo codigo
		continue #melhor opcao econtrada eh ignorar para que ele passe para o proximo
		
	comando = get_Last(elements)
	if comando == '':
		continue #ignorar quando comando nao existir
	if comando == 'up' or comando == 'UP' or comando == 'Up':
		print comando
		press_and_hold(k.up_key)
	elif comando == 'down' or comando == 'DOWN' or comando == 'Down':
		print comando
		press_and_hold(k.down_key)
	elif comando == 'right' or comando == 'RIGHT' or comando == 'Right':
		print comando
		press_and_hold(k.right_key)
	elif comando == 'left' or comando == 'LEFT' or comando == 'Left':
		print comando
		press_and_hold(k.left_key)
	elif comando == 'start' or comando == 'Start' or comando == 'START':
		print comando
		k.type_string('p')
	elif comando == 'select' or comando == 'Select' or comando == 'SELECT':
		print comando
		k.type_string('s')
	elif comando == 'b' or comando == 'B':
		print comando
		k.type_string('b')
	elif comando == 'a' or comando == 'A':
		print comando
		k.type_string('a')
	elif comando == 'X' or comando == 'x':
		print comando
		k.type_string('x')
	elif comando == 'Y' or comando == 'y':
		print comando
		k.type_string('y')
	elif comando == 'L' or comando == 'l':
		print comando
		k.type_string('l')
	elif comando == 'R' or comando == 'r':
		print comando
		k.type_string('r')
