# app.py

import sqlite3

# Connect to SQLite database (in-memory for simplicity)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Insert some data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John Doe', 25))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Jane Smith', 30))

# Query the data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
