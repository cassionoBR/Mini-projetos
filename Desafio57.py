print('Olá, informe seu sexo de acordo com as alternativas:\n[M] - MASCULINO ou [F] - FEMININO')
sexo = str(input('Seu sexo é: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('O sexo {} registrado com sucesso.'.format(sexo))
