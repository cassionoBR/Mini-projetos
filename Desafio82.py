num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip(' ')
    while resp[0] not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip(' ')
    if resp[0] not in 'Nn':
        continue
    break
print(f'Você digitou os números {num}')
for p, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores PARES digitados, foram {pares}')
print(f'Os valores ÍMPARES digitados, foram {impares}')
