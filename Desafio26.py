frase = str(input('Digite uma frase: ')).upper().strip()
a = frase.count('A')
b = frase.find('A')
c = frase.rfind('A')
print('Na frase a letra (a) se encontra {} vezes'.format(a))
print('Aparece pela primeira vez na posição {}'.format(b + 1))
print('Ultima vez que aparece é na posição {}.'.format(c + 1))

