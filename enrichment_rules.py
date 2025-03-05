# imports
import psycopg2

# database connection details
db_name = "alarm_db"
db_user = "postgres"
db_password = "Red123"
db_host = "localhost"
db_port = "5432"

# connect to database
def connect_db():
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    return conn, conn.cursor()

def fetch_unprocessed_alarms(cursor):
    # retrieve alarms that have not been enriched yet
    cursor.execute("SELECT alarm_id, site_id, alarm_code, severity FROM alarms WHERE alarm_id NOT IN (SELECT alarm_id FROM alarm_enrichment)")
    return cursor.fetchall()  # list of (alarm_id, site_id, alarm_code, severity)

def enrich_alarm(alarm):
    # apply the enrichment rules based on the alarm data
    alarm_id, site_id, alarm_code, severity = alarm

    # enrichment logic
    if severity == "Critical":
        additional_context = "Immediate technician dispatch required."
    elif severity == "Major":
        additional_context = "Escalate to network operations team."
    elif severity == "Minor":
        additional_context = "Monitor and review."
    else:
        additional_context = "No immediate action required."

    if alarm_code == "ALM001":
        site_info = f"Site {site_id} - Power Issue"
    elif alarm_code == "ALM002":
        site_info = f"Site {site_id} - Network Fault"
    elif alarm_code == "ALM003":
        site_info = f"Site {site_id} - Hardware Failure"
    else:
        site_info = f"Site {site_id} - Unknown Alarm Type"

    return (alarm_id, site_info, additional_context)

def insert_enriched_data(cursor, enriched_alarms):
    # insert the enriched alarm data into alarm_enrichment table
    cursor.executemany(
        "INSERT INTO alarm_enrichment (alarm_id, site_info, additional_context) VALUES (%s, %s, %s)",
        enriched_alarms
    )

def main():
    conn, cursor = connect_db()
    
    alarms = fetch_unprocessed_alarms(cursor)
    if not alarms:
        print("No new alarms to enrich.")
    else:
        enriched_alarms = [enrich_alarm(alarm) for alarm in alarms]
        insert_enriched_data(cursor, enriched_alarms)
        conn.commit()
        print(f"Enriched {len(enriched_alarms)} alarms successfully.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
