d = int((input('Digite a quantidade de dias que ficou com o carro? ')))
km = float(input('Digite quantos km(s), rodou nesses dias ?'))
print('De acordo com o que foi informado, o valor a se pagar é:R$ {:.2f}.'.format((d*60)+(km*0.15)))
