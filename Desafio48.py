s = 0
cont = 0
for imp in range(1, 501, 2,):
    if imp % 3 == 0:
        s = s + imp
        cont = cont + 1
print('A soma de todos os {} valores é {}'.format(cont, s))









