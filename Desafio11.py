alt = float(input('Altura da parede? '))
larg = float(input('Largura da parede? '))
area = alt * larg
print('De acordo com as medidas, sua dimenção é {}x{}. E área de {}'.format(alt,larg,area))
print('Para pintar sua parede, será necessário {}Lts de tinta.'.format(area/2))