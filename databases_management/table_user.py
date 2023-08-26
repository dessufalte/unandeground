import sqlite3 as sql
from config import AppConfig as con

def create_user_action(user_id):
    conn = sql.connect(con.U_A_DB)
    cursor = conn.cursor()
    
    table_name = f"user_action_{user_id}"
    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            action_id INTEGER PRIMARY KEY,
            action_type TEXT NOT NULL,
            thread_id INTEGER,
            parent_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (thread_id) REFERENCES threads (thread_id),
            FOREIGN KEY (parent_id) REFERENCES comments (comment_id)
        );
    """)
    
    conn.commit()
    conn.close()


