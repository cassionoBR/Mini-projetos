from datetime import date
hoje = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idad = hoje - nasc
if idad < 18:
    saldo = 18 - idad
    print('NÃO PODE se alistar, falta {} ano(s). Compareça em {}.'.format(saldo, hoje + saldo))
elif idad > 18:
    saldo = idad - 18
    print('Tempo para se alistar expirou a {} ano(s).'.format(saldo))
    print('Você devia ter se apresentado em {}.'.format(hoje - saldo))
else:
    print('Está na idade de se apresentar, compareça imediatamente!')