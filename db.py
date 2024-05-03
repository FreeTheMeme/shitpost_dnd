#old depercaded
import psycopg2
from datetime import datetime, timezone

username = 'postgres'
password = 'example'
host = '10.0.0.224'
port = 5432
database_name = 'shitpost_dnd'
dt = datetime.now(timezone.utc)

# Creates the users table
def addUserTable():
    conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
    )
    cur = conn.cursor()

    command = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(10),
        description TEXT,
        date_created TIMESTAMP
    );
    """
    cur.execute(command)
    conn.commit()
    conn.close()
# adds user
def addUserRow(name,description):
    conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
    )
    cur = conn.cursor()
        
    # SQL command to insert a row into the table
    insert_row_command = """
    INSERT INTO users (name, description, date_created)
    VALUES (%s, %s, %s);
    """


    # Execute the SQL command with the provided values
    cur.execute(insert_row_command, (name, description, dt))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


# Creates the charter table
def addCharterTable():
    conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
    )
    cur = conn.cursor()
    
    command = """
    CREATE TABLE IF NOT EXISTS charters (
        id SERIAL PRIMARY KEY,
        owner_name VARCHAR(10),
        charter_name VARCHAR(10),
        description TEXT,
        date_created DATE,
        level INT,
        max_Health INT,
        max_mana INT,
        current_Health INT,
        current_mana INT
    );
    """
    cur.execute(command)
    conn.commit()
    conn.close()

# Creates the charter table
def addItemTable():
    conn = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
    )
    cur = conn.cursor()
    
    command = """
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL PRIMARY KEY,
        owner_name VARCHAR(10),
        item_name VARCHAR(10),
        description TEXT,
        date_created DATE,
        Health_buff INT,
        mana_buff INT
    );
    """
    cur.execute(command)
    conn.commit()
    conn.close()
