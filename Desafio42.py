seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
print('ANALISANDO OS SEGMENTOS...')
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
   print('Forma um triangulo!')
   if seg1 == seg2 == seg3:
       print('Tipo: EQUILÁTERO')
   elif seg1 != seg2 != seg3 != seg1:
       print('Tipo: ESCACENO')
   else:
       print('Tipo: ISÓSELES')
else:
    print('Não forma um triangulo!')
