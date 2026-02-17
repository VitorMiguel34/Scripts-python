import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_PATH = ROOT / DB_NAME

con = sqlite3.Connection(DB_PATH)
cursor = con.cursor()

sql = '''CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)'''
cursor.execute(sql)

con.close()
