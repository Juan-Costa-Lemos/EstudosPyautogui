'''
Desafio: Ir até a pasta, clickar com o botão direito,
ir em nova pasta, clickar
'''
import pyautogui
import time

for i in range(7):
    #mover até pasta
    pyautogui.moveTo(967,253,duration=0.5)
    #clickar na pasta com botao direito
    pyautogui.rightClick()
    #ir até novo
    pyautogui.moveTo(1032,525,duration=0.5)
    time.sleep(1)
    #ir até pasta
    pyautogui.moveTo(754,281,duration=0.5)
    #clickar em novapasta
    pyautogui.click()
    pyautogui.doubleClick(1329,314)
    '''
    https://pastebin.pl/view/dfef88df

    '''