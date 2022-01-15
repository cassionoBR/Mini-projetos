salario = float(input('Quanto é o seu salário? R$: '))
if salario > 1250:
    novo = salario + (salario * 10/100)
else:
    novo = salario + (salario * 15/100)
print('O salário que era R${:.2f}, passa a ser R${:.2f}'.format(salario, novo))
