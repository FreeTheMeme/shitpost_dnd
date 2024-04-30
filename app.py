import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from datetime import datetime, timezone


load_dotenv()
app = Flask(__name__)
username = 'postgres'
password = 'example'
host = '10.0.0.224'
port = 5432
database_name = 'test'
#dt = datetime.now(timezone.utc)
connection = psycopg2.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    dbname=database_name
)


CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    return {"id": room_id, "message": f"Room {name} created."}, 201