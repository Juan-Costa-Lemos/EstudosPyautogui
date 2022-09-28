#simulando rolagem do mouse
from time import sleep
import pyautogui

pyautogui.moveTo(1015,457, duration=1.5)
pyautogui.click()
sleep(2)
#scrollando o mouse -desce + sobe
for i in range(100):
    pyautogui.scroll(-600)
