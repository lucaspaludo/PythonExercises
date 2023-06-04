

from math import hypot
cateto_adjascente = float(input('Digite o comprimento do cateto adjascente: '))
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
hi = hypot(cateto_oposto, cateto_adjascente)
print(f'O valor da hipotenusa vale: {hi:.2f}')

