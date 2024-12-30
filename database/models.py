from database.connection import get_connection

class Question:
    def __init__(self, id, question):
        self.id = id
        self.question = question

    def get_all():
        """Fetch all questions from the database."""
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM questions;")
            rows = cursor.fetchall()
            conn.close()
            return [Question(id=row[0], question=row[1]) for row in rows]

    def add(question_text):
        """Add a new question to the database."""
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO questions (question) VALUES (?)", (question_text,))
            conn.commit()
            conn.close()
