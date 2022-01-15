a = input('Digite seu nick ')
print('Tipo primitivo é:{}'.format(type(a)))
print('Contém números e/ou letras ? {}.'.format(a.isalnum()))
print('Contem somente letras? {}. '.format(a.isalpha()))
print('Contém somente números? {}.'.format(a.isnumeric()))
print('Está capitalizado? {}.'.format(a.istitle()))
print('Contém digitos? {}.'.format(a.isdigit()))
print('Está de acordo com o codigo "ASCII"? {}'.format(a.isascii()))
print('Está todo maiúsculo? {}.'.format(a.isupper()))
print('Está todo em minúsculo? {}.'.format(a.islower()))
print('É imprimivel? {}.'.format(a.isprintable()))


