pares = []
impares = []

for i in range(15):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
        if len(pares) == 5:
            print(f'Pares: {pares}')
            pares = []
    else:
        impares.append(n)
        if len(impares) == 5:
            print(f'Impares: {impares}')
            impares = []

if len(pares) > 0:
    print(f'Pares: {pares}')

if len(impares) > 0:
    print(f'Impares: {impares}')
