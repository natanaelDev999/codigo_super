import sqlite3 as sq
conexao = sq.connect('usuarios.db')
curso = conexao.cursor()
curso.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            sexo TEXT NOT NULL
            )''')
curso.execute('''SELECT * FROM usuarios''')
usuarios = curso.fetchall()
for usu in usuarios:
    print(f'indice: {usu[0]}')
    print(f'nome: {usu[1]}')
    print(f'idade: {usu[2]}')
    print(f'sexo: {usu[3]}')
conexao.commit()