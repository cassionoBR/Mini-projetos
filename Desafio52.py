numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1
        print('\033[31m {} '.format(c), end='')
    else:
        print('\033[m {}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(numero, total))
if total == 2:
    print('\033[31m{}\033[m Portanto é primo'.format(numero))
else:
    print('\033[31m{}\033[m Portanto não é primo!'.format(numero))