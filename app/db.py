import sqlite3
import os

DB_PATH = "data/visa.db"

os.makedirs("data", exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS visa_history (
        month TEXT PRIMARY KEY,
        final_action TEXT,
        filing TEXT,
        url TEXT
    )""")
    conn.commit()
    conn.close()

def insert_or_update(month, final_action, filing, url):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""INSERT OR REPLACE INTO visa_history VALUES (?, ?, ?, ?)""",
              (month, final_action, filing, url))
    conn.commit()
    conn.close()

def load_all():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM visa_history ORDER BY month")
    rows = c.fetchall()
    conn.close()
    return rows
