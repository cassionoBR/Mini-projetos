from random import randint
des = '\033[1m=-=\033[m'*20
print(f'{des}')
print('{:^60}'.format('VAMOS JOGAR PAR OU IMPAR'))
print(f'{des}')
v = 0
while True:
    jog = int(input('Digite um número: '))
    cpu = randint(1, 10)
    soma = cpu + jog
    tipo = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    while tipo not in 'PI':
        tipo = str(input('Opção invalída! PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {cpu}. Total {soma}')
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 != 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! você venceu {v} vezes!')
