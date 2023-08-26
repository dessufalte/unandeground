import sqlite3 as sql

def create_reply_comment_table(comment_id):
    conn = sql.connect('db/thd/kommen.db')
    cursor = conn.cursor()

    table_name = f"reply_thread_{comment_id}"
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            reply_id INTEGER PRIMARY KEY,
            comment_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (comment_id) REFERENCES thread_{comment_id} (comment_id)
        )
    ''')

    conn.commit()
    conn.close()

