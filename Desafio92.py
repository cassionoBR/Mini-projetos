from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['Ctps'] = int(input('Carteira de trabalho (0 - Não tem): '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] - nascimento) + 35
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
