from os import remove, system

def linha():
    print('-' * 50)

def cabecalho(txt):
    linha()
    print(f'{txt}'.center(50))
    linha()

def menu(*opcoes):
    for c in range(0, len(opcoes)):
        print(f'{c + 1} - {opcoes[c]}')

def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
            return num
        except:
            print('\033[31mNúmero inválido!\033[m')
        else:
            break

def leiaResposta(txt):
    while True:
        rsp = str(input(txt))
        if rsp == '':
            print('\033[31mEspaço em branco! Tente novamente!\033[m')
        else:
            return rsp
            break

def arquivoExiste(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except:
        return False
    else:
        return True

def criarArquivo(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        print('Erro ao criar o arquivo!')

def lerArquivo(arq):
    try:
        system('cls')
        arquivo = open(arq, 'rt')
        for linha in arquivo:
            elem = linha.split(';')
            if elem[0] == 'pergunta':
                cabecalho(elem[1].replace('\n', ''))
            else:
                print(elem[0], elem[1].replace('\n', ''))
        print('-' * 50)
        arquivo.close()
    except:
        print('Erro ao ler o arquivo!')
        