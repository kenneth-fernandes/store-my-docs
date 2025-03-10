import logging

from db import connect_db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User:
    def __init__(self, id, username, email, password_hash, role, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at


    @staticmethod
    def create_user(username, email, password, role="user"):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while creating user")
            return None
        try:
            password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, email, role, password_hash) "
                            "VALUES (%s, %s, %s, %s) RETURNING id;",
                            (username, email, role, password_hash))
                user_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            logging.info(f"New user created: {username} (user_id: {user_id})")
            return user_id
        except Exception as e:
            logging.error(f"User creation failed for {username}: {str(e)}")
            if conn:
                conn.close()
            return None


    @staticmethod
    def find_user_by_username_or_email(identifier):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while fetching user")
            return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE "
                            "username = %s OR email = %s;", (identifier, identifier))
                row = cur.fetchone()
            conn.close()
            if row:
                logging.info(f"User found for identifier = {identifier}")
                return User(*row)
            else:
                logging.warning(f"User not found for identifier = {identifier}")
                return None
        except Exception as e:
            logging.error(f"Failed to fetch user: {str(e)}")
            if conn:
                conn.close()
            return None


    @staticmethod
    def get_user_role(user_id):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while fetching user role")
            return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT role FROM users WHERE id = %s;", (user_id,))
                role = cur.fetchone()
            conn.close()
            if role:
                logging.info(f"User role found for user_id = {user_id}")
                return role[0]
            else:
                logging.warning(f"User role not found for user_id = {user_id}")
                return None
        except Exception as e:
            logging.error(f"Failed to fetch user's role: {str(e)}")
            if conn:
                conn.close()
            return None
