import sqlite3

# Initialize database and create users table
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)''')
# Insert a sample user (if not already present)
cursor.execute("INSERT OR IGNORE INTO users(username, password) VALUES (?, ?)", 
               ("admin", "admin123"))
conn.commit()
conn.close()

