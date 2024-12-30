import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Define questions to insert
questions = [
    # Personal Questions
    ('What is your firstname?', 'Personal'),
    ('What is your secondname?', 'Personal'),
    ('What did you study?', 'Personal'),
    ('What is your current job?', 'Personal'),
    
    # General Desktop vs Laptop Questions
    ('Why would you choose a desktop over a laptop?', 'Advantage'),
    ('What are the disadvantages of using a desktop?', 'Disadvantage'),
    
    # Device Usage
    ('What do you primarily use your computer for?', 'Usage'),
    ('How many hours a day do you use your computer?', 'Usage'),
    ('Do you require specific software that performs better on a desktop than on a laptop?', 'Usage'),
    
    # Cost
    ('What is your budget for a computer?', 'Cost'),
    ('Do you think a desktop is more cost-efficient than a laptop in the long run?', 'Cost'),
    
    # External Devices
    ('Do you use an external keyboard with your current device?', 'External Devices'),
    ('Do you use an external monitor with your current device?', 'External Devices'),
    ('How important is ergonomics to you?', 'External Devices'),
    
    # Mobility and Usability
    ('How important is portability in a computer for you?', 'Mobility'),
    ('Do you often need to use your computer in different locations?', 'Mobility'),
    ('Would you prefer your computer to always stay in one fixed location?', 'Mobility'),
    
    # Performance and Expandability
    ('How important is the ability to upgrade your device in the future?', 'Performance'),
    ('Which components do you consider most important for good performance?', 'Performance')
]

try:
    # Insert questions into the 'questions' table
    cursor.executemany('INSERT INTO questions (question_text, category) VALUES (?, ?)', questions)
    conn.commit()
    print("Questions added successfully!")
except sqlite3.Error as e:
    print("An error occurred:", e)
finally:
    conn.close()
