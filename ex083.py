while True:
    mat = input('Digite uma expressão matemática: ')
    if mat.count('(') == mat.count(')'):
        print('Sua expressão está correta!')
        break
    else:
        print('Você não digitou a expressão corretamente. Tente novamente')

