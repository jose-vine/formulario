from funcoes import *


linha()
print('FORMS'.center(50))
linha()
menu('Criar menu', 'Sair do sistema')
while True:
    opcao = leiaInt('Opção: ')
    if opcao == 1:
        print('Deu certo!')
        break
    elif opcao == 2:
        break
    else:
        print('\033[31mOpção inválida! Tente novamente!\033[m')
