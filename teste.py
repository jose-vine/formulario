from funcoes import *
from os import system

arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

system('cls')
cabecalho('FORMS')
menu('Criar menu', 'Executar formulário', 'Sair do sistema')
linha()
while True:
    opcao = leiaInt('Escolha uma das opções acima: ')
    if opcao == 1:
        system('cls')
        cabecalho('FORMS')
        formulario = dict()
        formulario['pergunta'] = leiaResposta('Informe a questão do seu formulário: ').strip()
        system('cls')
        cabecalho('FORMS')
        while True:
            alt = leiaInt(
                'Informe o número de alternativas do seu formulário: ')
            if alt == 2:
                system('cls')
                cabecalho('FORMS')
                formulario['a)'] = leiaResposta('Alternativa A: ').strip()
                formulario['b)'] = leiaResposta('Alternativa B: ').strip()
                system('cls')
                cabecalho('FORMS')
                while True:
                    formulario['resposta'] = leiaResposta('Informe a resposta correta da questão anterior: ').lower().strip()
                    if formulario['resposta'] in 'a' or formulario['resposta'] in 'b':
                        system('cls')
                        cabecalho('FORMS')
                        break
                    else:
                        print(
                            '\033[31mAlternativas inválidas! Por favor, informe corretamente!\033[m')
                break
            elif alt == 4:
                system('cls')
                cabecalho('FORMS')
                formulario['a)'] = leiaResposta('Alternativa A: ').strip()
                formulario['b)'] = leiaResposta('Alternativa B: ').strip()
                formulario['c)'] = leiaResposta('Alternativa C: ').strip()
                formulario['d)'] = leiaResposta('Alternativa D: ').strip()
                system('cls')
                cabecalho('FORMS')
                while True:
                    formulario['resposta'] = leiaResposta('Informe a resposta correta da questão anterior: ').lower().strip()
                    if formulario['resposta'] in 'a' or formulario['resposta'] in 'b' or formulario['resposta'] in 'c' or formulario['resposta'] in 'd':
                        system('cls')
                        cabecalho('FORMS')
                        break
                    else:
                        print('\033[31mAlternativas inválidas! Por favor, informe corretamente!\033[m')
                break
            else:
                print(
                    '\033[31mNúmero de alternativas inválido! Tente novamente!\033[m')
        arquivo = open(arq, 'at+')
        for k, v in formulario.items():
            arquivo.write(f'{k};{v}\n')
        arquivo.close()
        break
    elif opcao == 2:
        lerArquivo(arq)
        break
    elif opcao == 3:
        break
    else:
        print('\033[31mOpção inválida! Tente novamente!\033[m')
