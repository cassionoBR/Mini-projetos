import random
al = str(input('Nome do aluno: '))
al2 = str(input('Nome do aluno: '))
al3 = str(input('Nome do aluno: '))
al4 = str(input('Nome do aluno: '))
lista = [al, al2, al3, al4]
sorteio = random.choice(lista)
print('O resultado do sorteio é:{}'.format(sorteio))
