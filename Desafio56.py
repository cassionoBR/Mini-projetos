media = 0
maisv = 0
mulher = 0
idad = 0
for da in range(1, 5):
    print('---- {}ª PESSOA ----'.format(da))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Quantos anos você tem? '))
    print('Sexo:\n[M] - Masculino  [F] - Feminino')
    sexo = str(input('De acordo com as alternativas acima, informe seu sexo: ')).strip().upper()
    media += idade / 4
    if sexo == 'F' and idade < 20:
        mulher += 1
    else:
        if da == 1 and sexo == 'M':
            idad = idade
            maisv = nome
        elif sexo == 'M' and idade > da:
            idad = idade
            maisv = nome
print('''A média do grupo é de {} anos
O homem mais velho tem {} anos e se chama {}
Ao todo são {} mulheres, que tem menos de 20 anos'''.format(media, idad, maisv, mulher))

