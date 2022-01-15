from time import sleep


def maior(*num):
    cont = m = 0
    print('===' * 15)
    print('Analisando os valores passados...')
    for v in num:
        if cont == 0:
            m = v
        else:
            if v > m:
                m = v
        print(v, end=' ')
        sleep(0.5)
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
