import sqlite3

def create_db():
    conn = sqlite3.connect("users.db")  # Creates a database file
    cursor = conn.cursor()

    # Create a users table if it doesn’t exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')

    conn.commit()
    conn.close()

# Run this function to initialize the database
create_db()
print("Database created successfully.")
