from datetime import date
ano = int(input('Digite o ano em que nasceu: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Modalidade: MIRÍM'.format(idade))
elif idade <= 14:
    print('Modalidade: Infantil')
elif idade <= 19:
    print('Modalidade: Júnior'.format(idade))
elif idade <= 25:
    print('Modalidade: SÊNIOR'.format(idade))
else:
    print('Modalidade: MASTER'.format(idade))

