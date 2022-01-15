pt = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))
for c in range(pt, pt + 10 * ra, ra):
    print(c, '->', end=' ')
print('ACABOU')