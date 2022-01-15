def área(a, b):
    r = a * b
    print(f'A área de um terreno {a}x{b} é de {r:.1f}m².')


print('Controle de Terrenos')
print('===' * 10)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
área(larg, comp)
