print('\033[7;;41mGerador de Progressão Aritmética\033[m')
print('\033[1;31m=\033[m' * 33)
pt = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += ra
        cont += 1
    print('Pause')
    mais = int(input('Deseja saber mais quantos termo? '))
print('Programa finalizado com {} termos mostrados'.format(cont - 1))









