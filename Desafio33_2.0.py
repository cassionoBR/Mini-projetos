a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
          #verificando o menor!
menor = a
if a<b and b<c:
    menor = a
if b<a and a<c:
    menor = b
if c<a and a<b:
    menor = c
          #verificando o maior!
maior = a
if a>b and b>c:
    maior = a
if b>a and a>c:
    maior = b
if c>a and a>b:
    maior = c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
