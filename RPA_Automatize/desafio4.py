'''
Desafio
1) Navegar até o site https://cursoautomacao.netlify.app/
2) Encontar e clicar no campo "Digite seu nome" dentro de "Exemplos Alertas"
e digitar seu nome
3)Clicar em alerta, para gerar a alerta
4)fechar a alerta
5)Suba a pagina totalmente pra cima
6)Desca apenas o suficiente para conseguir chegar até a secção que conte
os arquivos o qual você ira fazer o download deles (totalmente pelo pyautogui)
clickar e movimentar o mouse da maneira que for necessaria para baixar os arquivosd e pdf
7) Depois de ter feito isso criar um alerta que diz que "Você terminou!!!"

'''
import pyautogui
import webbrowser
from time import sleep 
#1- Navegar ate o site 
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(2)
#2-Encontar o campo Exemplos alertas
pyautogui.click(678,443, duration=1.5)
pyautogui.scroll(-1100)
#3- localizar no digite seu nome
print(pyautogui.locateCenterOnScreen('RPA_Automatize/nome.png'))
#3.1 clickar em nome
pyautogui.click(pyautogui.locateCenterOnScreen('RPA_Automatize/nome.png'),duration=1.5)
#4- Digitar seu nome
pyautogui.typewrite('Juan Costa')
#5- Clickar em alerta 
print(pyautogui.locateCenterOnScreen('RPA_Automatize/alerta.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('RPA_Automatize/alerta.png'),duration=1)
#6- fechar o alerta
print(pyautogui.locateCenterOnScreen('RPA_Automatize/ok.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('RPA_Automatize/ok.png'),duration=1.5)
#7- Subir totalmente a pagina
pyautogui.click(678,443, duration=1.5)
pyautogui.scroll(1100)
sleep(1)
#8- Descer até a parte de download
for i in range(3):
    pyautogui.hotkey('PgDn')
    sleep(0.2)
#9- Clickar para fazer o download excel
print(pyautogui.locateCenterOnScreen('RPA_Automatize/excel.png'))
pyautogui.moveTo(pyautogui.locateCenterOnScreen('RPA_Automatize/excel.png'),duration=1)
pyautogui.scroll(-35)
sleep(0.5)
pyautogui.doubleClick()

#10- Clickar para fazer download do pdf
print(pyautogui.locateCenterOnScreen('RPA_Automatize/pdf.png'))
pyautogui.moveTo(pyautogui.locateCenterOnScreen('RPA_Automatize/pdf.png'),duration=1)
pyautogui.scroll(-35)
sleep(0.5)
pyautogui.doubleClick()

#11- Criar um alerta que diga que terminou
pyautogui.alert(text='VOCÊ TERMINOU!!',title='Automação finalizada',button='ok')
