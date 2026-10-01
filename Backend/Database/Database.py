import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        os.getenv("DATABASE_URL")
    )

def add_url (url):
    sql = "INSERT INTO url_handler (user_url) VALUES (%s) RETURNING id;"
    base_id = None
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (url,))
                rows = curr.fetchone()
                if rows:
                    base_id = rows[0]

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return base_id

def add_short_code (val, base_id):
    sql = '''
            UPDATE url_handler
            SET short_Code = (%s)
            WHERE id = (%s)
        '''
    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (val, base_id,))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

def check_code (code):
    sql = '''
            SELECT user_URL
            FROM url_handler
            WHERE short_code = (%s)
        '''

    try:
        with get_connection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (code, ))
                row = curr.fetchone()
                if row:
                    return row

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)