num = int(input('Digite um número par ou ímpar: '))
p = num % 2
print('Analisando o número {}.'.format(num))
if p == 0:
    print('Posso afirmar que ele é um número Par'.format(p))
else:
    print('Posso afirmar que ele é um número ímpar')
