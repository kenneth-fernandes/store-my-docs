import logging

from db import connect_db

class Document:
    def __init__(self, doc_id, filename, file_url, owner_id, uploaded_at):
        self.id = doc_id
        self.filename = filename
        self.file_url = file_url
        self.owner_id = owner_id
        self.uploaded_at = uploaded_at


    @staticmethod
    def get_all_documents():
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while fetching all documents")
            return []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM documents;")
                rows = cur.fetchall()
            cur.close()
            logging.info(f"Retrieved {len(rows)} documents")
            return [Document(*row).__dict__ for row in rows]
        except Exception as e:
            logging.error(f"Failed to fetch documents: {str(e)}")
            if conn:
                conn.close()
            return []


    @staticmethod
    def get_documents_by_user(owner_id):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while fetching documents for user")
            return []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM documents WHERE owner_id = %s;", (owner_id,))
                rows = cur.fetchall()
            cur.close()
            logging.info(f"Retrieved {len(rows)} documents for user_id: {owner_id}")
            return [Document(*row).__dict__ for row in rows]
        except Exception as e:
            logging.error(f"Failed to fetch user documents: {str(e)}")
            if conn:
                conn.close()
            return []


    @staticmethod
    def get_document_by_id(doc_id, owner_id):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while fetching document by doc_id and owner_id")
            return None
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM documents WHERE doc_id = %s AND owner_id = %s;", (doc_id, owner_id))
                row = cur.fetchone()
            conn.close()
            if row:
                logging.info(f"Retrieved document with doc_id: {doc_id} for user: {owner_id}")
                return Document(*row).__dict__
            else:
                logging.warning(f"Could not retrieve document with doc_id: {doc_id} for user: {owner_id}")
                return None
        except Exception as e:
            logging.error(f"Failed to fetch document: {str(e)}")
            if conn:
                conn.close()
            return None


    @staticmethod
    def insert_document(filename, file_url, owner_id):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while uploading document")
            return None

        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO documents (filename, file_url, owner_id) "
                            "VALUES (%s, %s, %s) RETURNING doc_id;", (filename, file_url, owner_id))
                doc_id = cur.fetchone()
            conn.commit()
            conn.close()
            logging.info(f"Document uploaded (doc_id: {doc_id}) by user_id: {owner_id}")
            return doc_id
        except Exception as e:
            logging.error(f"Failed to insert document: {str(e)}")
            if conn:
                conn.close()
            return None

    @staticmethod
    def delete_document(doc_id, user_id):
        conn = connect_db()
        if not conn:
            logging.error("Database connection failed while deleting document")
            return False
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM documents "
                            "WHERE doc_id = %s AND owner_id = %s RETURNING doc_id", (doc_id, user_id))
                deleted_doc_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            if deleted_doc_id:
                logging.info(f"Document deleted (doc_id: {doc_id}) by user_id: {user_id}")
                return True
            else:
                logging.warning(f"Document deletion unauthorized or not found "
                                f"(doc_Id: {doc_id}) for user_id: {user_id}")
                return False
        except Exception as e:
            logging.error(f"Failed to delete document: {str(e)}")
            if conn:
                conn.close()
            return False