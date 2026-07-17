
import tkinter as tk
logins = [['jujubinha','111'],
          ['pingu','222'],
          ['mymyn','4301'],
          ['teltel','0000000000000231']]

janela = tk.Tk()
janela.title('login')
janela.geometry('500x500')
pagina = tk.Frame(janela)
pagina.pack()
tk.Label(pagina,text='nome do usuario').pack()
nome = tk.Entry(pagina)

nome.pack()
tk.Label(pagina,text='senha').pack()
senha = tk.Entry(pagina,show='*')
senha.pack()

def cadastro():
    nome_usuario = nome.get()
    senha_usuario = senha.get()
    if nome_usuario == 'teltel' and senha_usuario == '999':
        pagina.pack_forget()
        janela_sistema.pack()
        mensagem['text'] = 'cadastrado com sucesso'
    elif [nome_usuario,senha_usuario] in logins:
        mensagem['text'] = 'cadastrado com sucesso'
    else:
        mensagem['text'] = 'conta inexistente'

tk.Button(pagina,text='verificação de usuario',command=cadastro).pack()
mensagem = tk.Label(pagina,text='')
mensagem.pack()
janela_sistema = tk.Frame()
tk.Label(janela_sistema,text='lista dos usuarios ').pack()
for usuario in logins:
    tk.Label(janela_sistema,text=f'{usuario}').pack()
janela.mainloop()

'''import tkinter as tk

# Lista de logins válidos (usuários comuns)
logins = [
    ('joão', '123'),
    ('maria', '1234'),
    ('mymyn', '4321'),
    ('yasmin', '231')
]

# Credenciais do dono do site
dono_login = ('teltel', '999')

# Janela principal
janela = tk.Tk()
janela.title('Login')
janela.geometry('500x500')

# Página inicial (login)
pagina = tk.Frame(janela)
pagina.pack()

tk.Label(pagina, text='Nome do usuário').pack()
nome = tk.Entry(pagina)
nome.pack()

tk.Label(pagina, text='Senha').pack()
senha = tk.Entry(pagina, show="*")  # senha oculta
senha.pack()

mensagem = tk.Label(pagina, text='')
mensagem.pack()

# Página do sistema (usuário comum)
janela_usuario = tk.Frame(janela)
mensagem_usuario = tk.Label(janela_usuario, text='')
mensagem_usuario.pack()

# Página especial (dono do site)
janela_dono = tk.Frame(janela)
tk.Label(janela_dono, text='Bem-vindo, dono do site!').pack()
tk.Label(janela_dono, text='Lista de usuários cadastrados:').pack()
for usuario in logins:
    tk.Label(janela_dono, text=f'{usuario[0]}').pack()  # mostra só o nome, não a senha!

# Função de verificação
def cadastro():
    nome_usuario = nome.get()
    senha_usuario = senha.get()

    if (nome_usuario, senha_usuario) == dono_login:
        pagina.pack_forget()
        janela_dono.pack()
    elif (nome_usuario, senha_usuario) in logins:
        pagina.pack_forget()
        mensagem_usuario['text'] = f'Bem-vindo, {nome_usuario}!'
        janela_usuario.pack()
    else:
        mensagem['text'] = 'Conta inexistente'

tk.Button(pagina, text='Verificação de usuário', command=cadastro).pack()

janela.mainloop()

import tkinter as tk
logins = [('joão','123'),
          ('maria','1234'),
          ('mymyn','4321'),
          ('yasmin','231')]

janela = tk.Tk()
janela.title('login')
janela.geometry('500x500')
pagina = tk.Frame(janela)
pagina.pack()
tk.Label(pagina,text='nome do usuario').pack()
nome = tk.Entry(pagina)

nome.pack()
tk.Label(pagina,text='senha').pack()
senha = tk.Entry(pagina)
senha.pack()
def cadastro():
    nome_usuario = nome.get()
    senha_usuario = senha.get()
    if nome_usuario == 'teltel' and senha_usuario == '999':
        pagina.pack_forget()
        janela_sistema.pack()
    if (nome_usuario,senha_usuario) in logins:
        mensagem['text'] = 'cadastrado com sucesso'
    else:
        mensagem['text'] = 'conta inexistente'

tk.Button(pagina,text='verificação de usuario',command=cadastro).pack()
mensagem = tk.Label(pagina,text='')
mensagem.pack()
janela_sistema = tk.Frame()
tk.Label(janela_sistema,text='lista dos usuarios ').pack()
for usuario in logins:
    tk.Label(janela_sistema,text=f'{usuario}').pack()
janela.mainloop()'''
'''import tkinter as tk

# Lista de logins válidos (usuários comuns)
logins = [
    ('joão', '123'),
    ('maria', '1234'),
    ('mymyn', '4321'),
    ('yasmin', '231')
]

# Credenciais do dono do site
dono_login = ('teltel', '999')

# Janela principal
janela = tk.Tk()
janela.title('Login')
janela.geometry('500x500')

# Página inicial (login)
pagina = tk.Frame(janela)
pagina.pack()

tk.Label(pagina, text='Nome do usuário').pack()
nome = tk.Entry(pagina)
nome.pack()

tk.Label(pagina, text='Senha').pack()
senha = tk.Entry(pagina, show="*")  # senha oculta
senha.pack()

mensagem = tk.Label(pagina, text='')
mensagem.pack()

# Página do sistema (usuário comum)
janela_usuario = tk.Frame(janela)
mensagem_usuario = tk.Label(janela_usuario, text='')
mensagem_usuario.pack()

# Página especial (dono do site)
janela_dono = tk.Frame(janela)
tk.Label(janela_dono, text='Bem-vindo, dono do site!').pack()
tk.Label(janela_dono, text='Lista de usuários cadastrados:').pack()
for usuario in logins:
    tk.Label(janela_dono, text=f'{usuario[0]}').pack()  # mostra só o nome, não a senha!

# Função de verificação
def cadastro():
    nome_usuario = nome.get()
    senha_usuario = senha.get()

    if (nome_usuario, senha_usuario) == dono_login:
        pagina.pack_forget()
        janela_dono.pack()
    elif (nome_usuario, senha_usuario) in logins:
        pagina.pack_forget()
        mensagem_usuario['text'] = f'Bem-vindo, {nome_usuario}!'
        janela_usuario.pack()
    else:
        mensagem['text'] = 'Conta inexistente'

tk.Button(pagina, text='Verificação de usuário', command=cadastro).pack()

janela.mainloop()'''