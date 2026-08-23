import tkinter as tk
import json
dados = []
pagina = None
saldo = 0.0
def linha():
    print('-'*40)
def cria_janela():
    global pagina
    janela = tk.Tk()
    janela.title('FinançasNT')
    janela.geometry('600x800')
    pagina = tk.Frame(janela)
    pagina.pack()
    return pagina
janela = cria_janela()
def salvar_dados(dados_recebidos):
    dados_json = {}
    print(dados_recebidos)
    with open("dados.json","r") as arquivo0:
        dados_json = json.load(arquivo0)
    dados_json[dados_recebidos[0]] = list(dados_recebidos[1:])
    with open("dados.json","w") as arquivo1:
        json.dump(dados_json,arquivo1)
def recebe_dados(pagina):
    # variáveis
    mes = ""
    aluguel = 0.0
    energia = 0.0
    gasolina = 0.0
    compras = 0.0
    roupas = 0.0
    internet = 0.0
    # recebe dados
    tk.Label(pagina, text='Digite o mês:').pack()
    mes = tk.Entry(pagina)
    mes.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com aluguel: ').pack()
    aluguel = tk.Entry(pagina)
    aluguel.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com energia: ').pack()
    energia = tk.Entry(pagina)
    energia.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com gasolinha: ').pack()
    gasolina = tk.Entry(pagina)
    gasolina.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com compras: ').pack()
    compras = tk.Entry(pagina)
    compras.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com roupas: ').pack()
    roupas = tk.Entry(pagina)
    roupas.pack()

    tk.Label(pagina, text='Digite quanto foi gasto com internet: ').pack()
    internet = tk.Entry(pagina)
    internet.pack()

    # total += aluguel + energia+gasolina+compras+roupas+internet
    return [aluguel,energia,gasolina,compras,roupas,internet,mes]
def visualizar_dados():
    total = 0
    for c in dados[0:-1]:
        if type(c) != float:
            print(c.get())
            v = c.get()
            total += float(v)
    lista_tipo = ['aluguel','energia','gasolina','compras','roupas','internet','mes']
    for pos,c in enumerate(dados):
        pagina.pack_forget()
        janela.pack()
        c = c.get()
        tk.Label(janela,text=f'{lista_tipo[pos]}:{"."*(10-len(c))}{c}').pack()
    tk.Label(janela,text=f'Total: {total}').pack()
    tk.Label(janela, text=f'Dinheiro restante:{"."*(10-len(str(total)))}{float(saldo.get())-total}').pack()
    dados_salvos = []
    for pos1,c in enumerate(dados):
        dados[pos1] = c.get()
    dados_salvos.append(dados[-1])
    dados_salvos.append(dados[0:-1])
    dados_salvos.append(total)
    salvar_dados(dados_salvos)
    dados.clear()
def main():
    global dados,saldo
    dados = recebe_dados(janela)
    tk.Label(janela, text='Dinheiro disponível: ').pack()
    saldo = tk.Entry(janela)
    saldo.pack()
    tk.Button(janela, text='visualizar e salvar', command=visualizar_dados).pack()
    janela.mainloop()
main()