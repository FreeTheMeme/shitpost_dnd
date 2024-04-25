import psycopg2
import passwords

users_count = 0
ip = '10.0.0.224'
def addrow(uesrs):
    conn = psycopg2.connect(database="resoniteUserCount",
                        host=ip,
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


def getdata(id):
    conn = psycopg2.connect(database="resoniteUserCount",
                        host=ip,
                        user="postgres",
                        password=passwords.DBpassword,
                        port="5432")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # SQL command to query all data from the table
    query = 'SELECT * FROM resoniteUserCount_data WHERE id ='+ str(id)

    # Execute the SQL command
    cur.execute(query)

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each one
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()