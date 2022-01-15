def fatorial(numero, show=False):
    """
    -> função > fatorial = Calcular fatorial de "numero".
    :param numero: O número a ser calculado(fatorial de 'numero')
    :param show: Opcional! Mostra ou não a conta.
    :return: O valor fatorial de "numero"
    """
    print('-=' * 20)
    fat = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end=' x ' if c > 1 else ' = ')
        fat *= c
    return fat


n = int(input('Digite um número para saber seu fatorial: '))
print(fatorial(n, show=True))
