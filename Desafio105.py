def notas(*num, sit=False):
    """
    :param num: média de cada aluno
    :param sit: Situação da media da sala ('Ruim', 'Regular', 'Boa')
    :return: Dicionario com informacões da turma
    """
    alunos = {'Total': len(num)}
    soma = 0
    situacao = {}
    for i, c in enumerate(num):
        if i == 0:
            alunos['Maior'] = c
            alunos['Menor'] = c
        else:
            if c > alunos['Maior']:
                alunos['Maior'] = c
            if c < alunos['Menor']:
                alunos['Menor'] = c
        soma += c
    alunos['Media'] = soma / len(num)
    if sit:
        if alunos['Media'] >= 7:
            situacao = 'Situação: Boa'
        elif 5 <= alunos['Media'] < 7:
            situacao = 'Situação: Regular'
        else:
            situacao = 'Situação: Ruim'
        return alunos, situacao
    else:
        return alunos


print(notas(7, 8, 4, 4.6, sit=True))
