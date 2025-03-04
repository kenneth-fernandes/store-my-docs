import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to PostgreSQL!")
        return conn
    except psycopg2.Error as e:
        print("Database connection failed:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    connect_db()