from Modulos_exercicios.Modulo_desafio108 import moedas

numero = float(input('Digite o preço: R$'))
aumentar = int(input('Quantos porcentos aumentar: '))

print(f'O dobro de {moedas.conversor(numero)} é {(moedas.dobro(numero, conv=True))}')
print(f'A metade de {moedas.conversor(numero)} é {(moedas.metade(numero, conv=True))}')
print(f'Aumentando {aumentar}% de {moedas.conversor(numero)},'
      f' temos {(moedas.aumentar(numero, aumentar, conv=True))}')
