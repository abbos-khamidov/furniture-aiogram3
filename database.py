import sqlite3

def init_db():
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            name TEXT,
            password TEXT
        )
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item TEXT,
        color TEXT,
        size TEXT,
        design TEXT,
        price INTEGER
    )""")
    conn.commit()
    conn.close()