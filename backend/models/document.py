from db import connect_db

class Document:
    def __init__(self, doc_id, filename, file_url, uploaded_at):
        self.id = doc_id
        self.filename = filename
        self.file_url = file_url
        self.uploaded_at = uploaded_at


    @staticmethod
    def get_all_documents():
        conn = connect_db()
        if not conn:
            return []
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT doc_id, filename, file_url, uploaded_at"
                            " FROM documents;")
                rows = cur.fetchall()
            cur.close()
            return [Document(*row).__dict__ for row in rows]
        except Exception as e:
            print("Failed to fetch documents:", e)
            if conn:
                conn.close()
            return []


    @staticmethod
    def get_document_by_id(doc_id):
        conn = connect_db()
        if not conn:
            return None

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT doc_id, filename, file_url, uploaded_at"
                            " FROM documents WHERE doc_id = %s;", (doc_id,))
                row = cur.fetchone()
            conn.close()
            return Document(*row).__dict__ if row else None
        except Exception as e:
            print("Failed to fetch document:", e)
            if conn:
                conn.close()
            return None

    @staticmethod
    def insert_document(filename, file_url):
        conn = connect_db()
        if not conn:
            return None

        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO documents (filename, file_url) "
                            "VALUES (%s, %s) RETURNING doc_id;", (filename, file_url))
                doc_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return doc_id
        except Exception as e:
            print("Failed to insert document:", e)
            if conn:
                conn.close()
            return None

    @staticmethod
    def delete_document(doc_id):
        conn = connect_db()
        if not conn:
            return False

        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM documents WHERE doc_id = %s RETURNING doc_id", (doc_id,))
                deleted_doc_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return deleted_doc_id is not None
        except Exception as e:
            print("Failed to delete document:", e)
            if conn:
                conn.close()
            return False