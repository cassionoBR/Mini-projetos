from Modulos_exercicios.utilidadesCeV import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.conversor(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.conversor(p)} é {moedas.dobro(p)}')
print(f'Aumentando 10% de {moedas.conversor(p)}, temos {moedas.aumentar(p, 10)}')
print(f'Reduzindo 50% de {moedas.conversor(p)}, temos {moedas.diminuir(p, 50)}')