num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado! não vou adicionar...')
    r = str(input('Quer continuar? ')).strip().upper()
    while r not in 'SN':
        print('Opção invalida!')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'Nn':
        break
print(f'Você digitou os valores {sorted(num)}')
