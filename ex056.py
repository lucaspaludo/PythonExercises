soma_idades = 0
media_idades = 0
maior_idade_masculina = 0
homem_mais_velho = ''
num_melher_21 = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA ----- ')
    nome = input('Digite o seu nome: ').strip()
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo: ').strip().upper()
    soma_idades += idade
    if i == 1 and sexo == 'MASCULINO':
       maior_idade_masculina = idade
       homem_mais_velho = nome
    if idade > maior_idade_masculina and sexo == 'MASCULINO':
        maior_idade_masculina = idade
        homem_mais_velho = nome
    if idade < 21 and sexo == 'FEMININO':
        num_melher_21 += 1

media_idades = soma_idades / 4
print(f'A média de idade do grupo é de {media_idades} anos')
print(f'O homem mais velho se chama {homem_mais_velho} e tem {maior_idade_masculina} anos')
print(f'{num_melher_21} mulheres tem menos de 21 anos')