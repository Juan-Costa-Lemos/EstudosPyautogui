#como pegar e "arrastar" algo para outro lugar

import pyautogui

for i in range(8):
    #mover até coord
    pyautogui.moveTo(920,142,duration=0.5)
    #Clicar e arrastar até o ponto e soltar ( apenas um comando)
    pyautogui.dragTo(901,676,duration=0.5)
    #repetir