a = float(input('Digite um comprimento: '))
b = float(input('Digite um comprimento: '))
c = float(input('Digite um comprimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triangulo!')
else:
    print('Não forma um triangulo!')