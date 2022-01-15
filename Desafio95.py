dados = list()
jogador = dict()
gols = []
while True:
    gols.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, Partidas):
        gols.append(int(input(f'   Quantos gols na {c + 1} partida? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    dados.append(jogador.copy())
    resposta = str(input('Quer continuar? [S/N] '))[0]
    while resposta not in 'NnSs':
        resposta = str(input('Quer continuar? [S/N] '))[0]
    if resposta in 'Nn':
        break
print('=-=' * 20)
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('===' * 20)
for i, v in enumerate(dados):
    print(f'{i:>3} ', end=' ')
    for valor in v.values():
        print(f'{str(valor):<15}', end='')
    print()
print('===' * 20)
while True:
    analisar = int(input('Mostrar dados de qual jogador? ([999] - Encerrar) '))
    if analisar == 999:
        break
    if analisar > len(dados) - 1:
        print(f'ERROR! jogador não encontrado no registro {analisar}')
    else:
        print(f'Levantamento do jogador {dados[analisar]["Nome"]}')
        for i, c in enumerate(dados[analisar]["Gols"]):
            print(f'   No {i + 1}º jogo, fez {c} gols')
    print('===' * 20)
print('<< Volte sempre >>')
