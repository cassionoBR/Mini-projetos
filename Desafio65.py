resp = 'S'
c = soma = media = ma = me = 0
while resp in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    c += 1
    resp = str(input('Quer continuar? ')).upper()[0].strip()
    if c == 1:
        ma = me = num
    elif num > ma:
        ma = num
    elif num < me:
        me = num
media = soma/c
print('Você digitou {} números e a média é {}'.format(c, media))
print('O maior valor é {} e o menor valor é {}'.format(ma, me))
