# imports
import psycopg2

# Connect to database
db_name = "alarm_db"
db_user = "postgres"
db_password = "Red123"
db_host = "localhost"
db_port = "5432"

connect_db = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

cursor = connect_db.cursor()

# delete all data from the table
cursor.execute("TRUNCATE TABLE sites RESTART IDENTITY CASCADE;")
connect_db.commit()  # Save changes

# Close connection
cursor.close()
connect_db.close()

print("All data deleted!")