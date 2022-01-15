while True:
    num = int(input('Digite um número: '))
    print('='*20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    print('='*20)
print('Programa finalizado, volte sempre!')
