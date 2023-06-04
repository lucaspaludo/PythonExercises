from random import randint
from time import sleep

numero_ecolhido = randint(0, 5) #gera um número aleatório entre 0 e 5

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)

numero_digitado = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if numero_ecolhido == numero_digitado:
    print('Parabéns! Você venceu')
else:
    print(f'Você perdeu! Eu pensei no número {numero_ecolhido} e você falou {numero_digitado}')


