num = []
while True:
    num.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar? ')).strip().upper()
    while cont not in 'SN':
        print('Opção inválida!', end='')
        cont = str(input('Quer continuar? ')).strip().upper()
    if cont == 'N':
        break
print(f'Você digitou {len(num)} elementos')
print(f'Os valores em ordem decrescente são {sorted(num, reverse=True)}')
print(f'O valor 5 faz parte da lista' if num.count(5)
      else 'O valor 5 não foi digitado!')
