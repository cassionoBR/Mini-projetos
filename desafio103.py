def ficha(jog=None, gol='0'):
    if jog == '':
        jog = '<desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {jog}, fez {gol} gols no campeonato.')


nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
ficha(nome, g)

#Outra solução
'''if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)'''
