import pyautogui

#Confirmar se uma automação deve continuar rodando
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?',title='Confirmação ', buttons=['sim','não','cancelar'])


if resposta == 'sim':
    print('sim')
elif resposta == 'não':
    print('não')
else:
    print('Operação cancelada')