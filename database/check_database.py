"""I had some issue's sith the database and didn't found the solution 
chatgpt recommend to use this file as a debug to see if there was something wrong with the database
"""


import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Check the tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the tables
print(tables)

# Close the connection
conn.close()