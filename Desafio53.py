frase = str(input('Digite uma frase: ')).strip().replace(' ', '')
contra = frase[::-1].replace(' ', '')
print('O inverso de {} é {}'.format(frase, contra))
if frase == contra:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')