nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print('\033[32mREPROVADO\033[m')
elif 7 > media >= 5:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[31mAPROVADO\033[m')
