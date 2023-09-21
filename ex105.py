def notas(*args, sit=False):
    """
    :param args: notas do aluno
    :param sit: situação do aluno (APROVADO, REPROVADO, EXAME)
    :return: dicionário informando a maior e menor nota, a média e situação do aluno
    """
    total = len(args)
    maior = max(args)
    menor = min(args)
    media = (args[0] + args[1] + args[2] + args[3]) / 4
    if media >= 7:
        situacao = 'APROVADO'
    elif 5 <= media < 7:
        situacao = 'EXAME'
    else:
        situacao = 'REPROVADO'
    if sit is False:
        ficha = {
            'total' : total,
            'maior' : maior,
            'menor' : menor,
            'media' : media
        }
        return ficha
    if sit:
        ficha = {
            'total': total,
            'maior': maior,
            'menor': menor,
            'media': media,
            'situacao': situacao
        }
        return ficha


resp = notas(10, 10, 3, 7, sit=True)
print(resp)
help(notas)
