nome = str(input('Digite seu nome: ').strip())
p = nome.split()
print('''Seu primeiro nome: {}.
Seu ultimo nome: {}.'''.format(p[0], p[-1]))