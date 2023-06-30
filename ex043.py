peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if (imc >= 12) and (imc < 18):
    print('Você está abaixo do peso.')
elif (imc >= 18) and (imc <= 24):
    print('Você está no peso ideal.')
elif (imc >= 25) and (imc <= 29):
    print('Você está gordo.')
elif (imc >= 30) and (imc <=39):
    print('Você está obeso.')
else:
    print('Você está morrendo')
