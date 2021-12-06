from funcoes import *
from os import system

system('cls')
cabecalho('FORMS')
menu('Criar menu', 'Sair do sistema')
linha()
while True:
    opcao = leiaInt('Escolha uma das opções acima: ')
    system('cls')
    cabecalho('FORMS')
    if opcao == 1:
        formulario = dict()
        formulario['pergunta'] = leiaResposta('Informe a questão do seu formulário: ')
        system('cls')
        cabecalho('FORMS')
        while True:
            alt=leiaInt('Informe o número de alternativas do seu formulário: ')
            linha()
            if alt == 2:
                formulario['a)'] = leiaResposta('Alternativa A: ')
                formulario['b)'] = leiaResposta('Alternativa B: ')
                system('cls')
                cabecalho('FORMS')
                while True:
                    resposta = leiaResposta('Informe a resposta correta da questão anterior: ')
                    if resposta.lower() in 'a' or resposta.lower() in 'b':
                        system('cls')
                        cabecalho('FORMS')
                        break
                    else:
                        print('\033[31mAlternativas inválidas! Por favor, informe corretamente!\033[m')
                break
            elif alt == 4:
                formulario['a)'] = leiaResposta('Alternativa A: ')
                formulario['b)'] = leiaResposta('Alternativa B: ')
                formulario['c)'] = leiaResposta('Alternativa C: ')
                formulario['d)'] = leiaResposta('Alternativa D: ')
                system('cls')
                cabecalho('FORMS')
                while True:
                    resposta = leiaResposta('Informe a resposta correta da questão anterior: ')
                    if resposta.lower() in 'a' or resposta.lower() in 'b' or resposta.lower() in 'c' or resposta.lower() in 'd':
                        system('cls')
                        cabecalho('FORMS')
                        break
                    else:
                        print('\033[31mAlternativas inválidas! Por favor, informe corretamente!\033[m')
                break
            else:
                print('\033[31mNúmero de alternativas inválido! Tente novamente!\033[m')
        for k, v in formulario.items():
            if k == 'pergunta':
                cabecalho(v)
            else:
                print(k, v)
        linha()
        break
    elif opcao == 2:
        break
    else:
        print('\033[31mOpção inválida! Tente novamente!\033[m')
