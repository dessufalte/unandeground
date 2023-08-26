import sqlite3 as sql
from config import AppConfig as con

def create_comment_table(thread_id):
    conn = sql.connect(con.K_DB)
    cursor = conn.cursor()
    
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS thread_{thread_id} (
            comment_id INTEGER PRIMARY KEY,
            thread_id INTEGER NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            upvotes INTEGER DEFAULT 0,
            parent_id INTEGER, -- ID komentar yang menjadi induk, NULL jika bukan balasan
            FOREIGN KEY (thread_id) REFERENCES threads (thread_id)
        )
    '''
    
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
