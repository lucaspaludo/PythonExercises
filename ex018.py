from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
rad = radians((angulo))
print(f"O seno de {angulo} é: {sin(rad):.2f}")
print(f"O cosseno de {angulo} é: {cos(rad):.2f}")
print(f"A tangente de {angulo} é: {tan(rad):.2f}")
