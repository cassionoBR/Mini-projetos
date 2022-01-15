from time import sleep


def ajuda(a):
    return help(a)


def titulo():
    print('\033[97;94;100m=' * 29)
    print('\033[97m|  Sistema de ajuda PyHELP |')
    print('=' * 29)


def subti(parametro):
    print('\033[90;101m=' * 32, end='')
    print('=' * len(parametro))
    print(f'\033[97m Acessando o manual do comando {parametro}\033[90m')
    print('=' * 32, end='')
    print('=' * len(parametro)), sleep(1)
    print(f'\033[m\033[30;107m')


while True:
    titulo()
    usuario = str(input('\033[mFunção ou biblioteca? '))
    subti(usuario)
    if usuario == 'FIM':
        print(f'\033[94;100m=' * 29)
        print(f'\033[97m        <<Até mais>>')
        print(f'\033[97m=' * 29)
        break
    help(usuario)
    sleep(1)
