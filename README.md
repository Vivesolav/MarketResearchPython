# Desktop vs Laptop: Een Vergelijkende Analyse

-Basic info

Dit project is een command-line applicatie die gebruikers vragen stelt over waarom ze een desktop boven een laptop zouden kiezen. De antwoorden worden opgeslagen in een SQLite-database en kunnen geëxporteerd worden naar een CSV- of Excel-rapport.

#Acties

- Vragenlijst via de terminal.
- Opslag van gebruikersantwoorden in een SQLite-database.
- Mogelijkheid om rapporten te genereren in CSV- of Excel-formaat.
- Gebruik van klassen voor een overzichtelijke structuur.


#Installatie
1. Clone de repository:
   https://github.com/Vivesolav/MarktonderzoekPython.git


2. Maak een virtuele omgeving:
   python -m venv venv
   
3. Activeer de virtuele omgeving:
   -.venv/Scripts/activate.bat (automatisch gegeven)


4. Installeer de vereisten:

   pip install -r requirements.txt


   cd database
   python create_database.py
   python insert_database.py 

#Applicatie starten
Start de applicatie vanuit de terminal:

   python main.py

Volg de instructies om vragen te beantwoorden en rapporten te genereren.


#Rapporten
De gegenereerde rapporten worden opgeslagen in de map `reports/`.

#Credits
Auteur: Olav Gryson-Modaert  
Email: olav.grysonmodaert@studen.vives.be
 