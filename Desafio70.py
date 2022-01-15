print('=='*20)
print('{} {:^18} {}'.format('>>'*5, 'Loja Virtual', '<<'*5))
print('=='*20)
total = totmil = menor = cont = 0
barato = resp = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Programa finalizado '))
print(f'''Total a pagar R${total:.2f}
{totmil} Produtos custando mais de R$1.000
Produto mais barato foi {barato} com o custo de R${menor:.2f}''')
