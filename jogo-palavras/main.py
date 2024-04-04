import random

palavras = [
    'abacate',
    'abacaxi',
    'carro',
    'casa',
    'computador',
    'celular',
    'bola',
    'boneca',
    'prato',
    'sapato',
    'sorvete'
]
menu = True
jogo = False

while menu:
    print('''
    [1] - Iniciar jogo
    [2] - Sair
    ''')
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print('Escolha uma opção válida!')
    else:
        if escolha == 1:
            print('Jogo iniciado! Para sair, digite 0 (zero).')
            jogo = True
            palavra = random.choice(palavras)
            palavra_underline = list('_' * len(palavra))
            for ln in palavra_underline:
                print(ln, end=' ')
            print()
            while jogo:
                letra = input('Digite uma letra: ').lower()
                if letra in palavra:
                    for i in range(len(palavra_underline)):
                        if palavra[i] == letra:
                            palavra_underline[i] = letra
                elif letra == '0':
                    jogo = False
                else:
                    print('Essa letra não existe na palavra. Tente de novo.')
                for ln in palavra_underline:
                    print(ln, end=' ')
                if '_' not in palavra_underline:
                    print()
                    print('Parabéns, você venceu!')
                    jogo = False
        else:
            print('Saindo...')
            menu = False
