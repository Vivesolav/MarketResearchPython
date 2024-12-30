import sqlite3
import csv
import os
from datetime import datetime

# Database configuration
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'questions.db')

if not os.path.exists(DB_PATH):
    raise FileNotFoundError(f"Database not found at {DB_PATH}")

RAPPORT_FOLDER = 'Reports'

os.makedirs(RAPPORT_FOLDER, exist_ok=True)

class SurveyApp:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.answers = []

    def get_questions(self):
        self.cursor.execute("SELECT question_text, category FROM questions")
        return self.cursor.fetchall()

    def ask_questions(self):
        print("\nStarting the survey. Please answer each question.\n")
        questions = self.get_questions()
        for question, category in questions:
            answer = input(f"{category} - {question}: ")
            self.answers.append((question, category, answer))

    def generate_csv_report(self):
        #Generate a CSV report with all answers.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"report_{timestamp}.csv"
        report_path = os.path.join(RAPPORT_FOLDER, report_filename)
        
        with open(report_path, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Question', 'Category', 'Answer'])
            csv_writer.writerows(self.answers)
        
        print(f"\nReport generated successfully!")
        print(f"File location: {os.path.abspath(report_path)}")

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    app = SurveyApp(DB_PATH)
    try:
        app.ask_questions()
        app.generate_csv_report()
    except KeyboardInterrupt:
        print("\n Survey interrupted by user.")
    finally:
        app.close()
