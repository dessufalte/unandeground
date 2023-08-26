import sqlite3 as sql
from flask import flash
from config import AppConfig as con
from databases_management import table_comment_reply as rply
from datetime import datetime
from functions import feature_profile as acc

def create_comment(thread_id, author, content, parent_id):
    r_author = acc.get_id_by_username(author)
    conn = sql.connect(con.K_DB)
    cursor = conn.cursor()
    try:
        cursor.execute(
            f'INSERT INTO thread_{thread_id} (thread_id, author, content, parent_id) VALUES (?, ?, ?, ?)',
            (thread_id, r_author, content, parent_id)
        )
        conn.commit()
        comment_id = cursor.lastrowid
        
        flash('Comment posted successfully!', 'success')
    except sql.Error as e:
        conn.rollback()
        flash('An error occurred while posting the comment.', 'error')
    finally:
        conn.close()


def get_comments(thread_id):
    conn = sql.connect(con.K_DB)
    cursor = conn.cursor()

    table_name = f"thread_{thread_id}"
    cursor.execute(f"SELECT * FROM {table_name} WHERE parent_id = '' OR parent_id = 0")
    comments = cursor.fetchall()
    
    user_conn = sql.connect(con.U_DB)
    user_cursor = user_conn.cursor()

    comments_with_pfp_and_date = []
    
    for comment in comments:
        author = comment[3] 
        r_author = acc.get_username_by_id(author)
        user_cursor.execute('SELECT pfp_image FROM user WHERE user_id = ?', (author,))
        pfp_image = user_cursor.fetchone()[0]

        comment_date = datetime.strptime(comment[2], "%Y-%m-%d %H:%M:%S").strftime("%d %B %Y")
        
        comment_with_pfp_and_date = comment + (pfp_image, comment_date,r_author) 
        comments_with_pfp_and_date.append(comment_with_pfp_and_date)
    conn.close()
    user_conn.close()
    
    return comments_with_pfp_and_date

def get_reply(thread_id):
    conn = sql.connect(con.K_DB)
    cursor = conn.cursor()

    table_name = f"thread_{thread_id}"
    cursor.execute(f"SELECT * FROM {table_name} WHERE parent_id != '' OR parent_id != 0")
    comments = cursor.fetchall()
    
    user_conn = sql.connect(con.U_DB)
    user_cursor = user_conn.cursor()

    comments_with_pfp_and_date = []
    
    for comment in comments:
        author = comment[3] 
        r_author = acc.get_username_by_id(author)
        user_cursor.execute('SELECT pfp_image FROM user WHERE user_id = ?', (author,))
        pfp_image = user_cursor.fetchone()[0]

        comment_date = datetime.strptime(comment[2], "%Y-%m-%d %H:%M:%S").strftime("%d %B %Y")
        
        comment_with_pfp_and_date = comment + (pfp_image, comment_date,r_author) 
        comments_with_pfp_and_date.append(comment_with_pfp_and_date)
    conn.close()
    user_conn.close()
    
    return comments_with_pfp_and_date

def create_reply(comment_id,author,content,parent_id):
        r_author = acc.get_id_by_username(author)
        conn = sql.connect(con.K_DB)
        cursor = conn.cursor()
        try:
            cursor.execute(
                f'INSERT INTO thread_{comment_id} (author, content, comment_id) VALUES (?, ?, ?)',
                (r_author, content, parent_id)
            )
            conn.commit()
            flash('reply posted successfully!', 'success')
        except sql.Error as e:
            conn.rollback()
            flash('An error occurred while posting the reply.', 'error')
        finally:
            conn.close()

def check_reply_thread_table_exist(table_name):
    conn = sql.connect(con.K_DB)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    
    result = cursor.fetchone()
    
    conn.close()
    
    return result
