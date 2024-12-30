import sqlite3

def create_database():
    conn = sqlite3.connect('questions.db')  
    cursor = conn.cursor()

    # Questions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT
    )
    ''')

    # Anwers atble
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER,
        answer TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(question_id) REFERENCES questions(id)
    )
    ''')

    conn.commit()
    conn.close()

create_database()
