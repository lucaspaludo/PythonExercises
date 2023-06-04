from random import choice

numero_digitado = int(input('Digite um número inteiro: '))
numero_escolhido = [0, 1, 2, 3, 4, 5]

escolha = choice(numero_escolhido)
print(f'O número escolhido foi {escolha}')

if numero_digitado == escolha:
    print('Você venceu!')
else:
    print('Você perdeu!')
