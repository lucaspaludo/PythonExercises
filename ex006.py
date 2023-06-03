cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m",
    "vermelho": "\033[31m",

}

num = int(input(f'{cores["amarelo"]}Digite um número:{cores["limpa"]} '))
print(f"O dobro de {num} é: {num*2} \nO triplo de {num} é: {num*3}")
print(f"A raíz quadrada de {num} é: {num**(1/2)}")
