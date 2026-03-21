def notas(*notas,situacao=False):
    '''
    essa função serve para a analise de notas
    que mostra total de notas maior nota menor nota e media e situação
    :param notas: recebe uma lista de notas escolares
    :param situacao:opcional que mostra a situação dos alunos
    :return:
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
notas = notas(10,4.5,6.9,5)
print(notas)