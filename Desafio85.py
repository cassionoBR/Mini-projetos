numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('=-'*25)
print(f'Números PARES digitados foram: {numeros[0]}')
print(f'Números IMPARES digitados foram: {numeros[1]}')
