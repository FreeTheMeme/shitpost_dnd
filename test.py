import psycopg2

# Replace with your database credentials
username = 'postgres'
password = 'example'
host = '10.0.0.224'
port = 5432
database_name = 'my_database'

conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
)

cur = conn.cursor()

# Create a new database
cur.execute("CREATE DATABASE my_new_database")

conn.commit()

conn.close()