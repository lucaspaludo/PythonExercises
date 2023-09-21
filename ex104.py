def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31m Erro! Digite um número inteiro. \033[m')
        if ok:
            break
    return valor


x = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {x}')
