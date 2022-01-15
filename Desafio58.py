#from random import randint
#cpu = randint(1, 10)
#print('{} JOGO DA ADVINHAÇÃO 2.0 {}'.format('==' * 15, '==' * 15))
#print('Tente adivinha o número que pensei (1 a 10).')
#jogador = int(input('Qual sua escolha: '))
#contagem = 0
#while jogador != cpu:
#    if jogador > cpu:
#        jogador = int(input('Menor!!, tente novamente: '))
#    elif jogador < cpu:
#        jogador = int(input('Maior!!, tente novamente: '))
#    contagem += 1
#print('Parabéns, você acertou! eu pensei no número {} e você precisou de {} tentativas.'.format(cpu, contagem +1))
from random import randint
cpu = randint(1, 10)
print('{} JOGO DA ADIVINHAÇÃO 2.0 {}'.format('==' * 12, '==' * 12))
print('Vou pensar num número de 1 a 10')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador > cpu:
            print('Tente um número menor!')
        elif jogador < cpu:
            print('Tente um número maior')
print('Acertou com {} tentativas'.format(palpite))
