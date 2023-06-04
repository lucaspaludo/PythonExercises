frase = input('Digite uma frase: ').strip()
print(f'Quantidade de letras "A": {frase.upper().count("A")}')
print(f'Posição que "A" aparece pela primeira vez: {frase.upper().find("A") + 1}')
print(f'Posição em que "A" aparece pela última vez: {frase.upper().rfind("A") + 1}')
