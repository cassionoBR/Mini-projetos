nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[1;31mREPROVADO\033[m! Estude mais.')
elif 7 > media >= 5:
    print('\033[1;33mRecuperação\033[m')
else:
    print('\033[1;32mAPROVADO\033[m! Parabéns!')