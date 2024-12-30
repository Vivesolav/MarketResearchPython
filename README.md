# Desktop vs Laptop: A Comparative Analysis

-Basic info

This project is a command-line application that asks users questions about why they would choose a desktop over a laptop. The answers are stored in a SQLite database and can be exported to a CSV or Excel report.

#Actions

- Questionnaire via the terminal.
- Storage of user answers in an SQLite database.
- Ability to generate reports in CSV or Excel format.
- Use of classes for a clear structure.

#Installation
1. Clone the repository:
https://github.com/Vivesolav/MarketResearchPython.git

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:
-.venv/Scripts/activate.bat (automatically provided)

4. Install the requirements:

pip install -r requirements.txt

cd database
python create_database.py
python insert_database.py

#Launch the application
Launch the application from the terminal:

python main.py

Follow the instructions to answer questions and generate reports.

#Reports
The generated reports are saved in the `reports/` folder.

#Credits
Author: Olav Gryson-Modaert
Email: olav.grysonmodaert@studen.vives.be