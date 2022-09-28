'''
Desafio ir até a pagina do wikipedia em historia do Brasil
'''

import pyautogui
from time import sleep

 #Essa automação foi executada com vscode dividsindo metade d tela
#clickar no navegado
pyautogui.moveTo(663,745, duration=0.5)
pyautogui.click()
sleep(2)
#ir até a guia de navegação
pyautogui.moveTo(969,59, duration=0.5)
#clicka na guia de navegação
pyautogui.click()
#digitar wikipedia brasil
pyautogui.typewrite('wikepedia brasil')

#apertar enter
pyautogui.hotkey('Enter')
#clickar no link
pyautogui.moveTo(884,377, duration=0.5)
pyautogui.click()
sleep(3)
#scrolar até a parte de historia
pyautogui.scroll(-4050)