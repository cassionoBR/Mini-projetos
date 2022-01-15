dados = []
soma = 0
while True:
    pessoas = dict()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip()
    while pessoas['sexo'] not in 'fFmM':
        pessoas['sexo'] = str(input('Sexo [M/F]: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    pessoas.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()
    while r not in 'NnSs':
        r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break
media = soma / len(dados)
mulheres = []
for i, c in enumerate(dados):
    if c['sexo'] in 'Ff':
        mulheres.append(c['nome'])
print('=-=' * 20)
print(f'-> O grupo tem {len(dados)} pessoas.'
      f'\n-> A média de idade é de {media:.2f} anos.'
      f'\n-> As mulheres cadastradas foram: {mulheres}')
print('Lista de pessoas acima da média:')
for c in dados:
    if c['idade'] >= media:
        print('  ')
        for k, v in c.items():
            print(f'  {k} = {v}', end=' ')
print('\n<< ENCERRADO >>')
