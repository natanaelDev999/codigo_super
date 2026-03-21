print('=-'*15, 'crie sua chave pix', '=-'*15)
import sqlite3
import random

nome = str(input('escreva seu nome: '))
idade = int(input('escreva sua idade: '))

if idade >= 18:
    conexao = sqlite3.connect("chaveis_pix.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        chave INTEGER UNIQUE
    )
    """)

    chave = 0
    while chave < 500:
        chave = random.randint(100, 10000)
        cursor.execute("SELECT * FROM usuarios WHERE chave = ?", (chave,))
        if cursor.fetchone() is None:
            break

    print(f"Sua chave Pix é: {chave}")

    cursor.execute("INSERT INTO usuarios (nome, idade, chave) VALUES (?, ?, ?)", (nome, idade, chave))
    conexao.commit()

    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    for r in registros:
        print(r)

    conexao.close()
else:
    print("Você precisa ter 18 anos ou mais para gerar uma chave Pix.")
