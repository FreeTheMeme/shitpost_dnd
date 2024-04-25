import psycopg2

# Replace with your database credentials
username = 'postgres'
password = 'example'
host = '10.0.0.224'
port = 5432
database_name = 'shitpost_dnd'

conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
)

cur = conn.cursor()

# Create
command = """
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    hire_date DATE
);
"""
cur.execute(command)

conn.commit()

conn.close()