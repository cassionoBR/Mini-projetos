print('Para finalizar o programa - [999]')
n = int(input('Digite um número: '))
c = m = 0
while n != 999:
    c += 1
    m += n
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles é {}'.format(c, m))
