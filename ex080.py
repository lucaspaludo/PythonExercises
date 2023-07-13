lista = []
num = lista.append(int(input('Digite um valor: ')))
print('Valor adicionado na posição 0')

for i in range(1, 5):
    num = int(input('Digite um valor: '))

    if i == 4:
        if num >= lista[3]:
            lista.insert(4, num)
            print('Valor adicionado na posição 4')
        elif lista[2] <= num < lista[3]:
            lista.insert(3, num)
            print('Valor adicionado na posição 3')
        elif lista[1] <= num < lista[2]:
            lista.insert(2, num)
            print('Valor adicionado na posição 2')
        elif lista[0] <= num < lista[1]:
            lista.insert(1, num)
            print('Valor adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Valor adicionado na posição 0')

    if i == 3:
        if num >= lista[2]:
            lista.insert(3, num)
            print('Valor adicionado na posição 3')
        elif lista[1] <= num < lista[2]:
            lista.insert(2, num)
            print('Valor adicionado na posição 2')
        elif lista[0] <= num < lista[1]:
            lista.insert(1, num)
            print('Valor adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Valor adicionado na posição 0')

    if i == 2:
        if num >= lista[1]:
            lista.insert(2, num)
            print('Valor adicionado na posição 2')
        elif lista[0] < num < lista[1]:
            lista.insert(1, num)
            print('Valor adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Valor adicionado na posição 0')

    if i == 1:
        if num >= lista[0]:
            lista.insert(1, num)
            print('Valor adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Valor adicionado na posição 0')
            
print('*=' * 20)
print(f'Os valores em ordem foram: {lista}')
