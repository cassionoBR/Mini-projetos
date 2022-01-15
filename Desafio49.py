print('{:^40}'.format(' Taboada da Multiplicação'))
num = int(input('Digite um valor para saber sua taboada: '))
for t in range(1, 11, 1,):
    print('{} x {:2} = {}'.format(num, t, num * t))
