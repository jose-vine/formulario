def linha():
    print('-' * 50)

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