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
        return rsp
        if rsp == '':
            print('\033[31mEspaço em branco! Tente novamente!\033[m')
        else:
            break
        