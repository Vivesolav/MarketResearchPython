import sqlite3

try:
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS questions")

    cursor.execute('''
    CREATE TABLE questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        category TEXT NOT NULL
    )
    ''')

    conn.commit()

    print("Table 'questions' created successfully!")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
    