import sqlite3

def get_connection():
    """Connection to the database."""
    try:
        conn = sqlite3.connect('questions.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None
