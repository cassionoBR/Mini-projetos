def escreva(txt):
    print(f'{"="}{"=" * len(txt)}{"="}')
    print(f' {txt}')
    print(f'{"="}{"=" * len(txt)}{"="}')


escreva(str(input('Frase: ')))
