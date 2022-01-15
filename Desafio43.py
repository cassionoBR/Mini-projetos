altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (Kg) '))
imc = peso / altura ** 2
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('CUIDADO! você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('PARABÉNS!você está com o peso ideal.')
elif 25 <= imc < 30:
    print('ATENCÃO! está acima do peso')
elif 30 <= imc < 40:
    print('ATENCÃO! você estar em obesidade')
else:
    print('CUIDADO! Obesidade mórbida')


