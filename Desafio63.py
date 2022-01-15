print('%=%'*20)
print('{:<5} {:^48} {:>5}'.format('%=', 'Sequência de Finobacci', '=%'))
print('%=%'*20)
num = int(input('>>>  Quantos termos deseja ver? '))
print('\033[1m{}\033[m'.format('~~') * 30)
t1 = 0
t2 = 1
cont = 3
if num == 1:
    print('0 -> Fim')
else:
    print('{} -> {}'.format(t1, t2), end=' -> ')
    while cont <= num:
        t3 = t1 + t2
        print(t3, end=' -> ')
        t1 = t2
        t2 = t3
        cont += 1
    print('Fim')
    print('~~' * 30)
