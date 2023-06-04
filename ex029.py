from time import strftime, localtime

horaAtual = strftime('%H.%M', localtime())
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está acima da velocidade, sua multa é de R$: {multa:.2f}')
    print(f'Hora do acontecimento: {horaAtual}')
else:
    print(f'Você está na velocidade adequada!')
    print(f'Hora do acontecimento: {horaAtual}')