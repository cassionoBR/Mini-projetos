num = int(input('Digite um número: '))
fato = 1
print('{}!= '.format(num), end='')
for c in range(num, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fato *= c
print(fato)
