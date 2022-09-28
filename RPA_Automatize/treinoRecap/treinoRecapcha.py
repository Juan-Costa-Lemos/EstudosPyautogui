from time import sleep
import pyautogui

#abrir navegador
pyautogui.hotkey('win')
#Procurar pelo microsoft edge
pyautogui.typewrite('Microsoft Edge')
#Acessar o edge
pyautogui.hotkey('enter')
sleep(1)
# buscar pagina
pyautogui.typewrite('recaptcha demo')
pyautogui.hotkey('enter')
sleep(1.5)
#entrar na pagina
pyautogui.click(881,355,duration=1)
#localizar o recaptcha
print(pyautogui.locateCenterOnScreen('RPA_automatize/treinoRecap/recaptcha.png'))
#clicar no recapcha
pyautogui.click(x=745, y=455,duration=1.5)
#localizar o enviar
print(pyautogui.locateCenterOnScreen('RPA_automatize/treinoRecap/enviar.png'))
#clickar no enviar
pyautogui.click(x=744, y=518, duration=1.5)