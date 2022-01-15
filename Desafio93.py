jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = []
for c in range(0, Partidas):
    gols.append(int(input(f'Quantos gols na {c + 1} partida? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('=-=' * 25)
print(jogador)
print('=-=' * 25)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}.')
print('=-=' * 25)
print(f'O jogador {jogador["Nome"]} jogou {Partidas} partidas ')
for c, g in enumerate(jogador["Gols"]):
    print(f'=> Na partida {c + 1}, fez {g} gols')
print(f'Foi um total de {jogador["Total"]}.')
