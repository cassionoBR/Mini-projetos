nome = input('Digite seu nome: ')
m = nome.upper(), nome.lower()
r = nome.replace(' ', '')
p = nome.split()
print('Nome maiúsculo e minúsculo: {}.'.format(m))
print('Total de letras do nome completo: {}. Do primeiro nome {}.'.format(len(r), len(p[0])))