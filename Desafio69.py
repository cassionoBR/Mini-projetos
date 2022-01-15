d = '=' * 29
print(F'''{d}
>>>> CADASTRE UMA PESSOA <<<<
{d}''')
tot18 = toth = totm = 0
sexo = cont = ''
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    print('='*29)
    cont = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    print('='*29)
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if cont == 'N':
        break
print(f'{d} RESULTADO DO PROGRAMA {d}')
print(f'''>Total de pessoas com mais de 18 anos: {tot18}
>Ao todo temos {toth} homens cadastrados
>E temos {totm} mulheres com menos de 20 anos''')
print(f'{d}= PROGRAMA FINALIZADO ={d}')
