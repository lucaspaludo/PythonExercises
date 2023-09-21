def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de alunos
    :param n: Uma ou mais notas (aceita várias)
    :param sit: Parâmetro opcional indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = round((sum(n)/len(n)), 2)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


#Programa principal
resp = notas(5.5, 2.5, 9, 8.5, 9, sit=True)
print(resp)
#help(notas)
