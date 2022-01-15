num1 = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito','Nove','Dez', 'Onze',
        'Doze', 'Treze', 'Cartoze', 'Quinze', 'Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cont = ''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente novamente! ', end='')
print(f'O número digitado foi {num1[num]}')
while True:
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont == 'N':
        print('Programa encerrado!')
        break
    else:
        if cont == 'S':
            num = int(input('Digite um número entre 0 e 20: '))
            print(f'O número digitado foi {num1[num]}')
