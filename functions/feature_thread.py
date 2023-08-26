import sqlite3 as sql
from datetime import datetime
from config import AppConfig as con
from databases_management import table_content as content_thread
from functions import feature_profile as acc
from functions import feature_preprocessing as pprc

def create_thread(content,author):
    title, tags, content_html = pprc.pprc_thread(content)
    id_user = acc.get_id_by_username(author)
    content_thread.insert_thread(id_user, content_html, tags, title)
    

def thread_viewer(date,author_idx):
    conn = sql.connect(con.T_DB)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM threads')
    threads = cursor.fetchall()

    conn.close()

    threads_with_pfp = []

    for thread in threads:
        author = thread[author_idx]
        thread_date = datetime.strptime(thread[date], "%Y-%m-%d %H:%M:%S").strftime("%d %B %Y")

        user_conn = sql.connect(con.U_DB)
        user_cursor = user_conn.cursor()
        user_cursor.execute('SELECT pfp_image FROM user WHERE user_id = ?', (author,))
        pfp_image = user_cursor.fetchone()
        user_conn.close()
        
        r_username = acc.get_username_by_id(author)
        if thread[3] is None or thread[3].strip() == "":
            thread_filter = thread[8]
        else:
            thread_filter = thread[3]
        thread_with_pfp = thread + (pfp_image[0],thread_date,r_username,thread_filter)
        threads_with_pfp.append(thread_with_pfp)
    
    return threads_with_pfp
