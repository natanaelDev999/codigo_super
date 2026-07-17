def notas(*notas,situacao=False):
    '''
    essa função serve para a análise de notas
    que mostra total de notas, maior nota, menor nota, média e situação.
    :param notas: recebe uma lista de notas escolares.
    :param situacao:opcional que mostra a situação dos alunos.
    :return: retorna as informações tratadas.
    '''
    informacoes = {'total de notas':len(notas),'maior nota':max(notas),'menor nota':min(notas),'media':sum(notas)/len(notas)}
    if situacao:
        if informacoes['media'] <= 5:
            informacoes['situação'] = 'ruim'
        elif informacoes['media'] > 7:
            informacoes['situação'] = 'ótima'
        else:
            informacoes['situação'] = 'boa'
    return informacoes
notas2 = notas(5.5,2.5,10,6.5,situacao=True)
help(notas)