num = int(input('Digite um número: '))

print('\033[33m-----------------------------\033[m')
print('\033[34mEscolha a forma de conversão:\033[m')
print('\t 1. Binário')
print('\t 2. Octal')
print('\t 3. Hexadecimal')
print('\033[33m-----------------------------\033[m')

escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida')
