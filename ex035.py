ladoA = float(input('Digite a medida do lado A: '))
ladoB = float(input('Digite a medida do lado B: '))
ladoC = float(input('Digite a medida do lado C: '))

if  ( (ladoB + ladoC) > ladoA > abs((ladoB - ladoC)) ) and ( (ladoA + ladoB) > ladoB > abs(ladoA - ladoC) ) and ( (ladoA + ladoB) > ladoC > abs(ladoA - ladoB) ):
    print('É possível formar um triângulo com os valores digitados!')
else:
    print('Não é possível formar um triângulo com os valores digitados')
