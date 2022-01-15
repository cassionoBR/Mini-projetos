aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).strip()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 25)
for k, v in aluno.items():
    print(f' {k} é igual a {v}')
