from random import randint
from time import sleep
print('='*40)
print(f'{"PALPITES DA MEGA-SENA":^40}')
print('='*40)
jogo = list()
sorteio = []
usuario = int(input('Quantos jogos quer que eu sorteie? '))
vz = 0
while vz < usuario:
    for c in range(0, 6):
        s = randint(0, 60)
        if s not in sorteio:
            sorteio.append(s)
        else:
            sorteio.append(randint(s + 1, 60))
    sorteio.sort()
    jogo.append(sorteio[:])
    sorteio.clear()
    vz += 1
print(f'{f"-=-=-=-=-=-=< Sorteando {usuario} jogos >=-=-=-=-=-=-":^40}')
for i, e in enumerate(jogo):
    print(f'Jogo {i + 1}: {e:>2}')
    sleep(1)
print(f'{"-=-=-=-=-=-=-=-=< BOA SORTE >=-=-=-=-=-=-=-=-":^45}')
