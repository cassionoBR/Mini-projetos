saque = int(input('Qual o valor do saque? R$'))
total = saque
cedula = 50
notas = 0
while True:
    if total >= cedula:
        total -= cedula
        notas += 1
    else:
        if notas > 0:
            print(f'{notas} cedúlas de R${cedula}')
        if cedula == 50:
            cedula = 20
        if cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        notas = 0
        if total == 0:
            break


#  print('''{}
#  {:^39}
#  {}'''.format('==' * 20, ' >>> Simulador de caixa eletrônico <<<', '==' * 20))
#  saq = int(input('Qual o valor de saque? '))
#  n50 = saq // 50
#  c = saq - 50 * n50
#  n20 = c // 20
#  n10 = v // 10
#  d = v - 10 * n10
#  n1 = d // 1
#  print('==' * 20)
#  print(f'''Total de {n50} cedúlas de R$50
#  total de {n20} cedúlas de R$20
#  Total de {n10} cedúlas de R$10
#  Total de {n1} cedúlas de R$1''')
#  print('VOLTE SEMPRE, TENHA UM BOM DIA!')