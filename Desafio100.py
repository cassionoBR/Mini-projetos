from random import randint
from time import sleep
numeros = list()


def sorteia(num):
    print('Sorteando os 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 19)
        num.append(n)
        print(n, end=' ')
        sleep(0.7)
    print('PRONTO!')


def somapar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores PARES de {num} é {soma}')


sorteia(numeros)
somapar(numeros)
