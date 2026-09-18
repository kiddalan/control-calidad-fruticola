import sqlite3

conn = sqlite3.connect("local.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pin TEXT,
    rol TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Base de datos local creada con exito")