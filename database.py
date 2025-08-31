import sqlite3

def init_db():
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            username TEXT,
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

# users

def add_user(tg_id, username, password):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (tg_id, username, password) VALUES (?, ?, ?)", (tg_id, username, password))
    conn.commit()
    conn.close()


def get_user(tg_id):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    user = cur.fetchone()
    conn.close()
    return user

# cart

def add_to_cart(user_id, item, color, size, design, price):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO cart (user_id, item, color, size, design, price) VALUES (?, ?, ?, ?, ?, ?)", (user_id, item, color, size, design, price))
    conn.commit()
    conn.close()

def get_cart(user_id):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cart WHERE user_id = ?", (user_id,))
    cart = cur.fetchall()
    conn.close()
    return cart