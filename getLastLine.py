from selenium import webdriver
import time
 
browser = webdriver.Firefox()
browser.get('http://www.twitch.tv/twitchplayspokemon')
  
# Para nao repetir o ultimo comando
blocker = 'init_blockRepeat'

raw_input("Press Enter to continue...")

# Lista <ul> com as msgs do chat
chatLineList = browser.find_element_by_id("chat_line_list")

while True:
	# Pega o ultimo elemento da chatLineList, 
	# armazena o Id do user na var currId,
	# e retorna o texto do comando. 

	try:
		lastEl = chatLineList.find_element_by_css_selector("li:last-child")
				
		if lastEl == blocker:
			continue
		else:
			# Pega o span com class='chat_line' e retorna o seu innerHTML
			span = lastEl.find_element_by_css_selector(".chat_line") 
			cmd = span.get_attribute("innerHTML")
			
			print cmd
		
	except Exception:
		continue
 



	
		