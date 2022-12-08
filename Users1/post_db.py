import sqlite3

def register(login, password1, password2):
    with sqlite3.connect('../Users.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        login VARCHAR(20),
                                                        password1 VARCHAR(20),
                                                        password2 VARCHAR(20))""")
        cursor.execute("""INSERT INTO users(login, password1, password2) VALUES(?, ?, ?)""", (login, password1, password2))
        db.commit()