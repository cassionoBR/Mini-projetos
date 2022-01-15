from math import hypot
cco = float(input('Comprimento do cateto oposto: '))
cca = float(input('Comprimento do cateto adjacente: '))
print('Comprimento da Hipotenusa é {:.2f}.'.format((hypot(cco, cca))))
