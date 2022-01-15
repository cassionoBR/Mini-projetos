num = int(input('Digite um número pra saber seu fatorial: '))
c = num
resultado = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= c
    c -= 1
print(resultado)