from random import randint
from time import sleep
print('=-_-='*15)
print('Vou pensar num número de 0 a 5, tente advinhar!')
print('=-_-='*15)
pc = randint(0, 5)
usuario = int(input('Digite o número eu pensei de (0 a 5): '))
print('PROCESSANDO...')
sleep(3)
if usuario == pc:
    print('PARABÉNS!, você acertou. Eu pensei o número {}'.format(pc))
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(pc, usuario))

