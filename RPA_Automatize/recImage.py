#reconhecimento de imagem simples com pyautogui
'''
snipping tool - ferramenta do wind para captura de imagens 

'''

import pyautogui

#localizar na tela as coordenadas, tem que estar no formato png
print(pyautogui.locateOnScreen('RPA_Automatize/numero_4.png'))

'''
Na minha tela foi reconhecido Box(left=725, top=496, width=76, height=49) com a loc da calculadora
'''

#encontrar a coordenada do centro da imagem 
print(pyautogui.locateCenterOnScreen('RPA_Automatize/numero_4.png'))

#na pratica do clickar
pyautogui.click(x=763, y=520, duration=1)

"""
!!! Importante esse reconhecimento de imagem é simples tem que ser bem limpa 
"""