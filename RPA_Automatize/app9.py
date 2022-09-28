#Recebendo senha de Usuario
from turtle import title
import pyautogui


senha = pyautogui.password(text='Digite sua senha',title='Dados de login', mask='*')

print(senha)