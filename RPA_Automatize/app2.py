#Como usar a função click
import pyautogui
#click personalizado
pyautogui.click(x=0,y=0,clicks=10,interval=0.1,button=2,duration=0.5)

#click na posição atual(com butão personalizado)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
#clickar x vezes
pyautogui.click(clicks=10)
#Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()