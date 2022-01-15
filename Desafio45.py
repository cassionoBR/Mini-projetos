from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=-=' * 10)
print('O computador jogou {}'.format(itens[cpu]))
print('O jogador jogou {}'.format(itens[jog]))
print('=-=' * 10)
if cpu == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('Jogador GANHOU!')
    elif jog == 2:
        print('Computador GANHOU!')
elif cpu == 1:
    if jog == 0:
        print('Computador GANHOU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('Jogador GANHOU!')
elif cpu == 2:
    if jog == 0:
        print('Jogador GANHOU!')
    elif jog == 1:
        print('Computador GANHOU!')
    elif jog == 2:
        print('EMPATE!')