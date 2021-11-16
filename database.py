import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text)")
        self.conn.commit()

    def register_user(self, username, password):
        self.cur.execute("INSERT INTO user VALUES (NULL, ?, ?)",
                         (username, password))
        self.conn.commit()

    def fetch_user(self, username, password):
        self.cur.execute("SELECT * FROM user WHERE username = ? AND password = ?",
                         (username, password))
        rows = self.cur.fetchall()
        return rows
