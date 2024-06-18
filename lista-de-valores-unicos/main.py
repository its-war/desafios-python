lista = set()

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    if n in lista:
        print('Esse número já foi digitado.')
    lista.add(n)

print(f'Valores que foram armazenados: {lista}')
