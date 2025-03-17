# This file is a Flask web application that retrieves alarm data from a PostgreSQL database and serves it via an API and a web page.

# imports
from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)

# Connect to database
DB_CONFIG = {
    "dbname": "alarm_db",
    "user": "postgres",
    "password": "Red123",
    "host": "localhost",
    "port": "5432"
}

def get_alarms():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = """
    SELECT 
        alarms.alarm_id, 
        alarms.alarm_code, 
        alarms.severity, 
        alarms.timestamp, 
        alarms.status, 
        sites.location, 
        sites.contact_info, 
        alarm_enrichment.site_info, 
        alarm_enrichment.additional_context 
    FROM alarms
    JOIN sites ON alarms.site_id = sites.site_id
    LEFT JOIN alarm_enrichment ON alarms.alarm_id = alarm_enrichment.alarm_id
    ORDER BY alarms.timestamp DESC;
    """
    
    cursor.execute(query)
    alarms = cursor.fetchall()

    conn.close()

    alarm_list = [
        {
            "alarm_id": row[0],
            "alarm_code": row[1],
            "severity": row[2],
            "timestamp": row[3].strftime("%Y-%m-%d %H:%M:%S"),
            "status": row[4],
            "location": row[5],
            "contact_info": row[6],
            "site_info": row[7],
            "additional_context": row[8]
        }
        for row in alarms
    ]

    return alarm_list

@app.route("/")
def home():
    return render_template("index.html")  # flask will look for `templates/index.html`

@app.route("/alarms", methods=["GET"])
def fetch_alarms():
    return jsonify(get_alarms())

if __name__ == "__main__":
    app.run(debug=True)
