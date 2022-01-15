preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço*5/100)
print('Valor do produto R${:.2f}. Com desconto de 5% = R${:.2f}.'.format(preço,novo))