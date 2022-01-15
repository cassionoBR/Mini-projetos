valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(f'Sua lista de números é {valores}')
print(f'O maior valor de sua lista é {max(valores)} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == max(valores) in valores:
        print(i, end=' ')
print(f'\nO menor valor de sua lista é {min(valores)} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == min(valores) in valores:
        print(i, end=' ')
