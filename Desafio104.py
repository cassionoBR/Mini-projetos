def leiaint(num):
    nume = input(num)
    while nume.isnumeric() is False:
        print('\033[31mERROR! Digite um número inteiro válido.\033[m')
        nume = input(num)
    else:
        nume = int(nume)
        return nume


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
