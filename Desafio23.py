num = int(input('Digite um número de 0 a 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('De acordo o numero {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar : {}'.format(m))
