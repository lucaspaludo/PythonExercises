palavras = ('Escadaria', 'Céu', 'Senhora', 'Branco', 'Ouro', 'Starbucks', 'Bateria')

for i in palavras:
    print(f'\nA palavra {i.upper()} contém as vogais', end=' ')
    for vogal in i:
        if vogal.lower() in 'aáãâàeéêèiíîìoóôõòuúûù':
            print(vogal.lower(), end=' ')

