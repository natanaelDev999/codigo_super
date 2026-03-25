import json
dados = {
    'nome':'natanael',
    'idade':11,
    'cidade':'americana'
}
with open('dados_json','w') as arquivo:
    json.dump(dados,arquivo,indent=4)
with open('dados_json','r') as arquivo:
    dados_json = json.load(arquivo)
print(dados_json)
dados_json['sexo'] = 'masculino'
with open('dados_json','w') as arquivo:
    json.dump(dados_json,arquivo,indent=4)
with open('dados_json','r') as arquivo:
    dados_json = json.load(arquivo)
print(dados_json)