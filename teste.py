from funcoes import *


linha()
print('FORMS'.center(50))
linha()
menu('Criar menu', 'Sair do sistema')
linha()
while True:
    opcao = leiaInt('Escolha uma das opções acima: ')
    linha()
    if opcao == 1:
        formulario = dict()
        formulario['pergunta'] = leiaResposta('Informe a questão do seu formulário: ')
        linha()
        while True:
            alt=leiaInt('Informe o número de alternativas do seu formulário: ')
            linha()
            if alt == 2:
                formulario['a)'] = leiaResposta('Alternativa A: ')
                formulario['b)'] = leiaResposta('Alternativa B: ')
                linha()
                while True:
                    resposta = leiaResposta('Informe a resposta correta da questão anterior: ')
                    if resposta.lower() in 'a' or resposta.lower() in 'b':
                        break
                    else:
                        print('\033[31mAlternativas inválidas! Por favor, informe corretamente!\033[m')
                break
            elif alt == 4:
                formulario['a)'] = leiaResposta('Alternativa A: ')
                formulario['b)'] = leiaResposta('Alternativa B: ')
                formulario['c)'] = leiaResposta('Alternativa C: ')
                formulario['d)'] = leiaResposta('Alternativa D: ')
                linha()
                while True:
                    resposta = leiaResposta('Informe a resposta correta da questão anterior: ')
                    if resposta.lower() in 'a' or resposta.lower() in 'b' or resposta.lower() in 'c' or resposta.lower() in 'd':
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
        break
    elif opcao == 2:
        break
    else:
        print('\033[31mOpção inválida! Tente novamente!\033[m')
