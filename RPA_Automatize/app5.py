#mandar mensagens/ escrever 
from time import sleep
import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

#Com o whats aberto 
#clicar em busca
pyautogui.click(874,183)
sleep(1)
#buscar contato
pyautogui.typewrite('Mozao')
#enviar
pyautogui.hotkey('enter')
#clickar no campo mensagem
pyautogui.click(1315,679)
sleep(1)
#enviar mensagem repetida
for i in range(50):
    escrever_frase('Meu Amor')
    pyautogui.hotkey('enter')
    sleep(0.1) 