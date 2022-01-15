from math import radians, sin, cos, tan
angulo = int(input('Digite um angulo: '))
sen = sin(radians(angulo))
print('O ângulo de {}° tem um seno de {:.2f}.'.format(angulo, sen))
cos = cos(radians(angulo))
print('O ângulo de {}° tem um coseno de {:.2f}.'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {}° tem o tangente de {:.2f}'.format(angulo, tan))
