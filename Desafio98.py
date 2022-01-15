from time import sleep


def contador(i, f, p):
    print('===' * 10)
    print(f'Contador de {i} a {f} de {p} em {p}: ')
    print('===' * 10)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        pos = 0
        while pos <= f:
            print(pos, end=' ')
            sleep(0.5)
            pos += p
        print()
    if i > f:
        pos = i
        while pos >= f:
            print(pos, end=' ')
            sleep(0.5)
            pos -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez! pode personalizar a vontade.')
ini = int(input('Inicio: '))
fi = int(input('Final: '))
pa = int(input('Passo: '))
contador(ini, fi, pa)
