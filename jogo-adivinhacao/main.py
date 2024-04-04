import random
menu_ativo = True

numero = random.randint(1, 1000)

while menu_ativo:
    print('Tente adivinhar o número (digite Q para sair):')
    try:
        escolha = int(input('> '))
    except ValueError:
        print('Saindo do programa...')
    else:
        if numero == escolha:
            print('Parabéns, você acertou!!')
            menu_ativo = False
        elif numero > escolha:
            print('Tente um número maior!')
        else:
            print('Tente um número menor!')
