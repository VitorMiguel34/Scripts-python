import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_PATH = ROOT / DB_NAME

with sqlite3.connect(DB_PATH) as con:
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL CHECK(preco>0)
    )''')
    con.commit()

    insert_sql = "INSERT INTO Produtos (nome,preco) VALUES (:nome,:preco)"
    cursor.execute(insert_sql,{"nome":"arroz","preco":6})
    con.commit()

    cursor.execute("SELECT * FROM Produtos")
    for produto in cursor.fetchall():
        print(produto)

