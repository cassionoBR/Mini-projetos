s = 0
con = 0
for re in range(0, 6):
    num = int(input('Digite seis números inteiros: '))
    if num % 2 == 0:
        s = s + num
        con = con + 1
print('Você informou {} números pares e a soma deles é igual a {}'.format(con, s))

