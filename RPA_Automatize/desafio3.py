'''
Desafio criar uma automação que pede ao usuario login e senha, abra o bloco de notas e salva em um bloco de notas

'''

from time import sleep
import pyautogui

#Pedir para o usuario digitar login
login = pyautogui.prompt(text='Digite seu login',title='Dados de login')
#Pedir para o usuario digitar senha
senha = pyautogui.password(text='Digite sua senha',title='Dados de login',mask='*')
#Abrindo comandos
pyautogui.hotkey('win','r')
#digitar notepad
pyautogui.typewrite('notepad')  
#aperta o enter 
pyautogui.press('enter')
sleep(1)
#colar os dados
pyautogui.typewrite(f'login: {login} \n')
pyautogui.typewrite(f'senha: {senha} \n')


