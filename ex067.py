produto = 0
print('---#---'*10)
num = int(input('Digite um número para ver a sua tabuada: '))
print('---#---'*10)
if num > 0:
    while True:
        for i in range(1, 11):
            produto = num * i
            print(f'{num} * {i} = {produto}')
        print('---#---' * 10)
        num = int(input('Digite um número para ver a sua tabuada: '))
        print('---#---' * 10)
        if num < 0:
            print('FIM.')
            break
else:
    print('FIM.')
