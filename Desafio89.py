alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    alunos.append(nome, [nota1, nota2], media)
    r = str(input('Quer continuar? ')).strip()
    while r not in 'SsNn':
        r = str(input('Quer continuar? ')).strip()
    if r in 'Nn':
        break
print('===' * 25)
print('No.  Nome:      Média:')
print('=-='*18)
for i, c in enumerate(alunos):
    print(f'{i:<3}|  {c[0]:<8} {c[2]:>10}')
print('=-='*18)
ver_notas = None
while ver_notas != 999:
    ver_notas = int(input('Gostaria de ver as nota de qual aluno? [999]-Encerrar '))
    if ver_notas <= len(alunos):
        print(f'Notas de {alunos[ver_notas][0]} são {alunos[ver_notas][1]}')
        print('---'*15)
    else:
        print('Aluno não cadastrado')
    if ver_notas == 999:
        print('>>>Finalizado, volte sempre!<<<')
        break
