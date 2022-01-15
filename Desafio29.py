vel = float(input('Qual a velocidade marcada pelo radar? '))
if vel >= 81:
    print('Você foi multado!. Sua multa vai custar R${:.2f}'.format((vel - 80) * 7))
else:
    print('Você não ultrapassou o limite!')
