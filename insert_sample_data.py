# imports
import psycopg2
import random
import subprocess # to run enrichment_rules.py

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
    ("New York", "contact@nyc.com", 1),
    ("Los Angeles", "contact@la.com", 2),
    ("Chicago", "contact@chi.com", 3),
]

cursor.executemany("INSERT INTO sites (location, contact_info, priority) VALUES (%s, %s, %s)", sites)

# insert sample alarm data
alarm_codes = ["ALM001", "ALM002", "ALM003"]
severities = ["Critical", "Major", "Minor", "Warning"]

for _ in range(10):
    cursor.execute(
        "INSERT INTO alarms (site_id, alarm_code, severity) VALUES (%s, %s, %s)",
        (random.randint(1, len(sites)), random.choice(alarm_codes), random.choice(severities))
    )

connect_db.commit()  # save changes to the database

# run enrichment_rules.py file
subprocess.run(["python", "enrichment_rules.py"])

# save changes to db and also close the cursor and connection
#connect_db.commit()  # save changes to the database
cursor.close()
connect_db.close()

print("Data inserted successfully!")