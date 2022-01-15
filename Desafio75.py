numeros = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor "9" apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número "3" apareceu na {numeros.index(3)+1}ª posição')
else:
    print('Não foi digitado o número "3"')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
