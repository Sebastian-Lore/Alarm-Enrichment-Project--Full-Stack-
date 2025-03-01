# imports
import psycopg2
import random

# connect to database
db_name = "alarm_db"
db_user = "postgres"
db_password = "Red123"
db_host = "localhost"
db_port = "5432"

connect_db = psycopg2.connect(
    dbname = db_name,
    user = db_user,
    password = db_password,
    host = db_host,
    port = db_port
) # end of function connect_db 

cursor = connect_db.cursor() # create a cursor to run SQL queries

# insert sample site data
sites = [
    (100, "New York", "contact@nyc.com", 1),
    (101, "Los Angeles", "contact@la.com", 2),
    (102, "Chicago", "contact@chi.com", 3),
]

cursor.executemany("INSERT INTO sites (site_id, location, contact_info, priority) VALUES (%s, %s, %s, %s)", sites)

connect_db.commit()  # this is required to save changes to the database

print("Data inserted successfully!")

# Close the cursor and connection
cursor.close()
connect_db.close()