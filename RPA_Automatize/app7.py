import pyautogui

#Pedindo informação ao usuario

email = pyautogui.prompt(text='Digite seu email', title='informações obrigatorias')

print(f'Você digitou {email}')
