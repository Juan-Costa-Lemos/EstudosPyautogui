# Alerta e pedir informação 
from tkinter import Button
import pyautogui

pyautogui.alert(text='Iniciando sua automação',title='Automação de login',button='ok')

#exibe todas as teclas do teclado
print(pyautogui.KEYBOARD_KEYS)