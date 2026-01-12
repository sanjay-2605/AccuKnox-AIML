import sqlite3, csv

conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

with open("users.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                    (row['name'], row['email']))

conn.commit()
conn.close()
