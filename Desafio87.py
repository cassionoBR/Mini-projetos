matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = soma_linha = 0
for c in range(0, 3):
    for b in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {b}]: '))
        if n % 2 == 0:
            pares += n
        matriz[c][b] = n
    soma += matriz[c][2]
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print('-='*25)
print(f'A soma dos valores pares: {pares}')
print(f'A Soma dos valores da 3ª coluna: {soma}')
for c in range(0, 3):
    if c == 0:
        soma_linha = matriz[1][c]
    elif matriz[1][c] > soma_linha:
        soma_linha = matriz[1][c]
print(f'O maior valor da 2ª linha: {soma_linha}')
