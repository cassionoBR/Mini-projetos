from Modulos_exercicios.Modulo_desafio107 import moedas

p = float(input('Digite o preço: R$'))
aumentar = int(input('Digite a porcentagem para aumentar: '))
diminuir = int(input('Digite a porcentagem para reduzir: '))
print(f'A metade de {moedas.conversor(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.conversor(p)} é {moedas.dobro(p)}')
print(f'Aumentando {aumentar}% em {moedas.conversor(p)}, temos {moedas.aumentar(p, aumentar)}')
print(f'Reduzindo {diminuir}% em {moedas.conversor(p)}, temos {moedas.diminuir(p, diminuir)}')
