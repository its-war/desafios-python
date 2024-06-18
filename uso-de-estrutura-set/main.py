lista = []
repetidos = set()

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    if n in lista:
        repetidos.add(n)
    lista.append(n)

print(f'Número que se repetiram: {repetidos}')
