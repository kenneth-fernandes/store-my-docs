import logging

import psycopg2
from config import DB_CONFIG

def connect_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logging.info("Connected to PostgreSQL!")
        return conn
    except psycopg2.Error as e:
        logging.error(f"Database connection failed: {str(e)}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    connect_db()