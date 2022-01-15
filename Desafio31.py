km = float(input('Quantos km até seu destino? '))
print('Você está prestes a começar uma viagem de {}km.'.format(km))
if km <= 200:
    print('Total a pagar R${:.2F}'.format(km * 0.50))
else:
    print('Total a pagar R${:.2F}'.format(km * 0.45))

