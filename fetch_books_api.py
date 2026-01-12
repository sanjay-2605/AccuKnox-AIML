import requests, sqlite3

# Sample API fetch (mock URL)
books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008}
]

conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INT)")

for b in books:
    cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                (b['title'], b['author'], b['year']))

conn.commit()
conn.close()
print("Books stored successfully")
