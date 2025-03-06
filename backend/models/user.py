from db import connect_db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User:
    def __init__(self, id, username, email, password_hash, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at


    @staticmethod
    def create_user(username, email, password):
        conn = connect_db()
        if not conn:
            return None
        try:
            password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, email, password_hash) "
                            "VALUES (%s, %s, %s) RETURNING username;",
                            (username, email, password_hash))
                user_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return user_id
        except Exception as e:
            print("Failed to create user:", e)
            if conn:
                conn.close()
            return None


    @staticmethod
    def find_user_by_username_or_email(identifier):
        conn = connect_db()
        if not conn:
            return None

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE "
                            "username = %s OR email = %s", (identifier, identifier))
                row = cur.fetchone()
            conn.close()
            return User(*row) if row else None
        except Exception as e:
            print("Failed to fetch user:", e)
            if conn:
                conn.close()
            return None
