from datetime import date
ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual! '))
if ano == 0:
    ano = date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto.')
