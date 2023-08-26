import sqlite3 as sql
from config import AppConfig as con

def record_user_action(user_id, action_type, thread_id=None, parent_id=None):
    conn = sql.connect(con.U_A_DB)
    cursor = conn.cursor()
    
    table_name = f"user_action_{user_id}"
    
    cursor.execute(f"""
        INSERT INTO {table_name} (action_type, thread_id, parent_id)
        VALUES (?, ?, ?)
    """, (action_type, thread_id, parent_id))
    
    conn.commit()
    conn.close()
    
def check_user_action(user_id, action_type, thread_id=None, parent_id=None):
    try:
        conn = sql.connect(con.U_A_DB)
        cursor = conn.cursor()

        table_name = f"user_action_{user_id}"

        query = 'SELECT COUNT(*) FROM {} WHERE action_type = ?'.format(table_name)
        params = [action_type]

        if thread_id is not None:
            query += ' AND thread_id = ?'
            params.append(thread_id)
        if parent_id is not None:
            query += ' AND parent_id = ?'
            params.append(parent_id)

        cursor.execute(query, params)
        count = cursor.fetchone()[0] 

        return count > 0 
    except sql.Error as e:
        print('Error:', e)
        return False
    finally:
        conn.close()

def delete_user_action(user_id, action_type, thread_id=None, parent_id=None):
    try:
        conn = sql.connect(con.U_A_DB)
        cursor = conn.cursor()

        table_name = f"user_action_{user_id}"

        query = f"DELETE FROM {table_name} WHERE action_type = ?"
        params = [action_type]

        if thread_id is not None:
            query += " AND thread_id = ?"
            params.append(thread_id)
        if parent_id is not None:
            query += " AND parent_id = ?"
            params.append(parent_id)

        cursor.execute(query, params)
        conn.commit()
    except sql.Error as e:
        print('Error:', e)
    finally:
        conn.close()

def delete_user_action_exists(user_id, action_type, thread_id=None, parent_id=None):
    if check_user_action(user_id, action_type, thread_id=thread_id, parent_id=parent_id):
        delete_user_action(user_id, action_type, thread_id=thread_id, parent_id=parent_id)
