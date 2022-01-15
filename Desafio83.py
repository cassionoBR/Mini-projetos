exp = str(input('Faça sua expressão: '))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expresão está correta!')
else:
    print('A expresão está incorreta!')
