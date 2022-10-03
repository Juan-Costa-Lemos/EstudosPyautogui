from time import sleep
import pyautogui

import webbrowser
'''
Esse bot foi executado em tela cheia no meu computador com uma resolução de 1336x768.

'''

def sair():
    #sai da publicação
    pyautogui.click(1319,98, duration=2)
    #Clickar no perfil
    pyautogui.click(1132,100, duration=2)
    sleep(3)
    #Clickar em sair da conta
    pyautogui.click(969,347, duration=2) 
    #fechar a pagina
    pyautogui.click(1342,17,duration=2)
    #pausar por 24 horas
    sleep(86400)

def curtir():
    sleep(3)
    pyautogui.click(356,701,duration=2)
    sleep(3)
    pyautogui.click(675,571,duration=2)
    sleep(2)
    pyautogui.click(712,569,duration=2)
    sleep(2)
    pyautogui.typewrite('Gostei dessa foto!')
    sleep(3)
    pyautogui.click(1105,677, duration=2)

login = pyautogui.prompt(text='Digite seu login', title='Informações obrigatorias')
senha = pyautogui.password(text='Digite sua senha', title='Informações obrigatorias')

def logar():
    # Entrar com meu usuario
    pyautogui.click(849,270,duration=2)
    pyautogui.typewrite(f'{login}')
    # Entrar com a senha
    pyautogui.click(846,311,duration=2)
    pyautogui.typewrite(f'{senha}')
    # Clickar em login 
    pyautogui.click(861,359,duration=2)
    sleep(3)
    # not now
    pyautogui.click(675,473,duration=2)
    sleep(3)
    #fechar janelinha de salvar senha
    pyautogui.click(845,80,duration=2)

pagina = pyautogui.prompt(text='Digite a pagina de busca para o bot curtir e comentar a primeira publicação', title='Informações obrigatorias')

def pesquisa():
    pesquisar = pyautogui.locateCenterOnScreen('pesquisar.png')
    pyautogui.click(pesquisar,duration=2)
    # Pesquisar/digitar pagina 
    pyautogui.typewrite(f'{pagina}')
    sleep(3)
    # Entrar na pagina
    pyautogui.move(0,80,duration=2)
    pyautogui.click()
    sleep(3) 
    # Encontrar postagem mais recente
    pyautogui.click(347,687, duration=2)
    sleep(3)
    


while True:
        # 1 - Navegar até o insta
        webbrowser.open_new_tab('https://www.instagram.com/')
        sleep(5)
        #logando
        logar()
        # localizar pesquisar
        pesquisa()
        # 8 - Verificar se esta curtida ou não a postagem 
        # 9 - Se já tiver curtido não fazer nada
        curtido = pyautogui.locateCenterOnScreen('curtido.png')
        if curtido is not None:
            sair()
        # 11 - Se não tiver curtido, curtir a foto
        # 12 - se não tiver comentado, comentar
        elif curtido == None:
            curtir()
            sair()
