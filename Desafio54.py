from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idad = atual - ano
    if idad < 21:
        menor += 1
    elif idad >= 21:
        maior += 1
print('Ao todo tivemos {} pessoas de menores!'.format(menor))
print('E {} Pessoas são maiores'.format(maior))