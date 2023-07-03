num = int(input('Digite um número inteiro: '))
for c in range(2, num):
    if num % c == 0:
        print(f'O número {num} não é primo')
        break
else:
    print(f'O número {num} é primo!')
