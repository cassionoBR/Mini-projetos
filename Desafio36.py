casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto é o seu salário mensal? R$'))
anos = int(input('Em quantos anos pretende quitar o ímovel? '))
pres = casa / (anos * 12)
print('Para comprar uma casa no valor de R${} em {} anos. a prestação fica de {:.2f}'.format(casa, anos, pres))
if pres > (salario*30/100):
    print('\033[31mNEGADO')
else:
    print('PARABÉNS! Seu emprestimo foi \033[1;32mAPROVADO\033[m')