import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS lamparas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE,
        circuito TEXT,
        estado TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS mantenimientos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        codigo_lampara TEXT,
        tipo TEXT,
        descripcion TEXT,
        foto TEXT
    )
    """)

    conn.commit()
    conn.close()

def insertar_lamparas():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    circuitos = {
        "C1":5,
        "C2":5,
        "C3":15,
        "C4":5,
        "C5":5,
        "C6":5,
        "C7":5,
        "C8":5,
        "C9":5,
        "C10":5,
        "C11":5,
        "C12":5
    }

    for circuito,cantidad in circuitos.items():

        for i in range(1,cantidad+1):

            codigo = f"{circuito}-L{i}"

            c.execute("""
            INSERT OR IGNORE INTO lamparas
            (codigo,circuito,estado)
            VALUES(?,?,?)
            """,(codigo,circuito,"Operativa"))

    conn.commit()
    conn.close()
