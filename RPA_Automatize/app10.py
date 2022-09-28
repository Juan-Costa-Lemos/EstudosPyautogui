#Tirando print da tela inteira ou parte dela
import pyautogui

#print tela inteira
pyautogui.screenshot('tela.jpg')

#Print lugar especifico
'''Para isso vamos usar o mouseInfo e captar a coordenada inicial, 
ver quantos pixel devemos andar para direita e para baixo. O retante sera autocompletado pelo pyautogui  '''
pyautogui.screenshot('regiao.jpg',region=(975,101,320,534)) 