import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Execute the table creation queries here if you want programmatically
    with open('sql/create_tables.sql', 'r') as f:
        cursor.execute(f.read())
    
    conn.commit()
    conn.close()
