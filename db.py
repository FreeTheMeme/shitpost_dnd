import psycopg2
import passwords

username = 'postgres'
password = 'example'
host = '10.0.0.224'
port = 5432
database_name = 'shitpost_dnd'

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
        date_created DATE
    );
    """
    cur.execute(command)
    conn.commit()
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




def addrow(uesrs):
    conn = psycopg2.connect(database="resoniteUserCount",
                        host=host,
                        user="postgres",
                        password=passwords.DBpassword,
                        port="5432")

    cur = conn.cursor()

    insert_script = 'INSERT INTO resoniteUserCount_data (users, time) VALUES (%s, %s)'
    insert_value = (uesrs, "now")
    cur.execute(insert_script, insert_value)
    conn.commit()

    cur.close()
    conn.close()
    print("added row ",uesrs," here")