def voto(ano):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos o voto é NEGADO'
    elif 18 <= idade <65:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'
    else:
        return f'Com {idade} anos o voto é OPCIONAL'


nasc = int(input('Em que ano você nasceu? '))
res = voto(nasc)
print(res)
