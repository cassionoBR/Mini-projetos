pessoas = list()
dados = []
pesado = maneiro = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))

    resp = str(input('Quer continuar? [S/N] ')).strip()
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'SsNn':
        resp = str(input('Quer continuar: [S/N] ')).strip()
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
for i, v in enumerate(pessoas):
    if i == 0:
        pesado = v[1]
        maneiro = v[1]
    else:
        if v[1] > pesado:
            pesado = v[1]
        if v[1] < maneiro:
            maneiro = v[1]
print(f'Maior peso foi {pesado}kg. Peso de', end=' ')
for v in pessoas:
    if v[1] == pesado:
        print(f'[{v[0]}]', end=' ')
print(f'\nMenor peso foi {maneiro}kg. Peso de', end=' ')
for c in pessoas:
    if c[1] == maneiro:
        print(f'[{c[0]}]', end=' ')
