produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'{"=="*23}\n'
      f'{"LISTAGEM DE PREÇOS":^46}\n'
      f'{"=="*23}\n')
for c in range(0, len(produtos[::2])):
    print(f'{produtos[::2][c]}.........................R${produtos[1::2][c]:.2f}')
print(f'{"=="*23}')


########################-RESPOSTA_GUANABARA-###########################

produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'{"=="*23}\n'
      f'{"LISTAGEM DE PREÇOS":^46}\n'
      f'{"=="*23}\n')
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<20}', end='')
    else:
        print(f'{produtos[c]:.>20.2f}')