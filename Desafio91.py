from time import sleep
from random import randint

jogadores = {'jogador_1': [randint(1, 6)], 'jogador_2': [randint(1, 6)],
             'jogador_3': [randint(1, 6)], 'jogador_4': [randint(1, 6)]}
for k, c in jogadores.items():
    print(f'O {k} tirou {c}')
cont = 1
for c in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{cont}º lugar: {c} com {jogadores[c]}')
    cont += 1
