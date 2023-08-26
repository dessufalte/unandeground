import sqlite3 as sql
from databases_management import table_comment as comment
from flask import flash
from config import AppConfig as con


thread_db = con.T_DB

def create_threads_table():

    conn = sql.connect(thread_db)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS threads (
        thread_id INTEGER PRIMARY KEY,
        date TEXT DEFAULT CURRENT_TIMESTAMP,
        author TEXT NOT NULL,
        isithread TEXT NOT NULL,
        upvotes INTEGER DEFAULT 0,
        downvotes INTEGER DEFAULT 0,
        views INTEGER DEFAULT 0,
        tags TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_thread(author, content_html, tags, title):
    try:
        conn = sql.connect(thread_db)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO threads (author, isithread, tags, title) VALUES (?, ?, ?, ?)',
                       (author, content_html, ', '.join(tags), title))
        conn.commit()
        thread_id = cursor.lastrowid
        comment.create_comment_table(thread_id)
        return thread_id

    except sql.Error as e:
        conn.rollback()
        flash('An error occurred while creating the thread.', 'error')
    finally:
        conn.close()