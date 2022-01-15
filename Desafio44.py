print(f'{" SARDINHAS LOJAS ":=^40}')
preco = float(input('Preço das compras? '))
print('''Forma de pagamento: 
[1]-AVISTA
[2]-AVISTA NO CARTÃO 
[3]-2X NO CARTÃO
[4]-3X OU MAIS NO CARTÃO.''')
pag = int(input('Escolha a forma de pagamento: [1] [2] [3] [4]: '))
if pag == 1:
    total = preco - (preco * 10/100)
    print('Preço do produto R${} C/ Desconto de 10% = R${:.2f}'.format(preco, total))
elif pag == 2:
    total = preco - (preco * 5/100)
    print('Preço do produto R${} C/ Desconto de 5% = R${:.2f}'.format(preco, total))
elif pag == 3:
    total = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(total))
    print('O valor de sua compra sem acrecímos R${:.2f}'.format(preco))
elif pag == 4:
    parcela = int(input('Quantas parcelas? '))
    total = (preco + (preco * 20/100))
    qp = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcela, qp))
    print('Sua compra de R${:.2f}. Vai custar R${:.2f} no final'.format(preco, total))
else:
    print('\033[31mFORMA DE PAGAMENTO INVÁLIDA\033[m! ')
