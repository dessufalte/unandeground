import os
import sqlite3 as sql

def delete_thread_data():
    try:
        conn = sql.connect('db/thread.db')
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM threads')
        conn.commit()
        conn.close()
        
        print("Data in 'threads' table deleted successfully.")
    except sql.Error as e:
        print("An error occurred while deleting data:", str(e))

import os
import sqlite3 as sql

def delete_kommen_tables():
    try:
        kommen_db_path = 'db/thd/kommen.db'
        
        if os.path.exists(kommen_db_path):
            conn = sql.connect(kommen_db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                cursor.execute(f"DROP TABLE {table_name};")

            conn.commit()
            conn.close()
            
            print("All tables in 'kommen.db' deleted successfully.")
        else:
            print("Kommen database does not exist.")
    except Exception as e:
        print("An error occurred while deleting tables:", str(e))

delete_thread_data()
delete_kommen_tables()
