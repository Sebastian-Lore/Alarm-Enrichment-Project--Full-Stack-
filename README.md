# Alarm Enrichment Project (Full Stack)
 
This project is a full-stack alarm monitoring system that:
- Inserts randomized alarm data into a PostgreSQL database.
- Enriches alarms with additional context.
- Provides a REST API to fetch alarm data.
- Displays alarms in a web-based dashboard.

Technologies Used:
- Backend: Python, Flask, PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Database Library: psycopg2
- Web Framework: Flask

Project Structure:
- insert_sample_data.py: Inserts random alarm data into PostgreSQL
- enrichment_rules.py: Processes & enriches alarms
- retrieve_data.py: Flask API to serve alarm data
- index.html (in templates folder): Frontend dashboard
- delete_sample_data: Deletes all data from the database.

How to run:
- Step 1) Install Dependencies: pip install -r requirements.txt
- Step 2) Set Up PostgreSQL Database: SQL to create the tables is inside the create_tables.sql file
- Step 3) Run insert_sample_data.py: python insert_sample_data.py
- Step 4) Start the Flask Server: python retrieve_data.py
- Step 5) Open the Dashboard: Visit http://127.0.0.1:5000/ in your browser to view the Alarm Dashboard. ( a link should appear in the terminal that you can click)
- Step 6) End the program: press ctrl + c on the terminal. 
