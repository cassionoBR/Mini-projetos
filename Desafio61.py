pt = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))
termo = pt
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += ra
    c += 1
print('FIM')
