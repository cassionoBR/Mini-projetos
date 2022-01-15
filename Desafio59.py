pri = int(input('Digite o primeiro valor: '))
seg = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('''    Auto menu:
[1]-Somar
[2]-Multiplicar
[3]-Saber o maior
[4]-Novos números
[5]-Sair do programa 
>>>> Qual sua opção? '''))

    if menu == 1:
        print('A soma de {} e {} é igual a {}'.format(pri, seg, pri + seg))
    elif menu == 2:
        print('{} multiplicado por {} é igual a {}'.format(pri, seg, pri * seg))
    elif menu == 3:
        if pri > seg:
            print('{} é maior que {}'.format(pri, seg))
        elif seg > pri:
            print('{} é maior que {}'.format(seg, pri))
        else:
            print('{} e {} são iguais'.format(pri, seg))
    elif menu == 4:
        pri = int(input('Digite um novo número: '))
        seg = int(input('Digite um novo número: '))
    elif menu > 5:
        print('Opção inválida. Tente novamente! ')
    print('==₢==' * 7)
print('Programa finalizado. Até mais!')