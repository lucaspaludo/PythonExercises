print('\033[33m='*15, '\033[M \033[32mBANCO PALUDO\033[M', '\033[33m='*15, '\033[m')
valorDoSaque = int(input('Qual valor você deseja sacar? R$'))
valorRestante = valorDoSaque
cedula = 50
totalCedula = 0
while True:
    if valorRestante >= cedula:
        valorRestante -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'{totalCedula} cédulas de R${cedula}')
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if totalCedula == 0:
            break
print('\033[33m='*15, '\033[M \033[32mOBRIGADO! VOLTE SEMPRE!\033[M', '\033[33m='*15, '\033[m')
