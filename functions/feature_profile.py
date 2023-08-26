import sqlite3 as sql
from flask import flash
from config import AppConfig as con
from secure_information import crypt
from databases_management import table_user as rec
 
def update_profile(current_username, new_username, new_password, new_biography):
    key = crypt.generate_key()
    hashed_password = crypt.encrypt_message(new_password,key)
    try:
        conn = sql.connect(con.U_DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE user SET username=?, password=?, biography=? WHERE username=?',
                       (new_username, hashed_password, new_biography, current_username))
        conn.commit()
    except sql.Error as e:
        conn.rollback()
        flash('An error occurred while updating the profile.', 'error')
    finally:
        conn.close()

def check_existing_username(username):
    conn = sql.connect(con.U_DB)
    cursor = conn.cursor()

    cursor.execute('SELECT username FROM user WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    conn.close()
    return existing_user is not None

def get_username_by_id(user_id):
    conn = sql.connect(con.U_DB)
    cursor = conn.cursor()
    
    cursor.execute('SELECT username FROM user WHERE user_id = ?', (user_id,))
    username = cursor.fetchone()[0]
    
    conn.close()
    return username

def get_id_by_username(username):
    conn = sql.connect(con.U_DB)
    cursor = conn.cursor()
    
    cursor.execute('SELECT user_id FROM user WHERE username = ?', (username,))
    username = cursor.fetchone()[0]
    
    conn.close()
    return username

def create_account(username, password):
    pfp_image = con.DEFAULT_PFP
    relation_foll = 0
    relation_following = 0
    threads_total = 0
    biography = ''
    key = crypt.generate_key()
    hashed_password = crypt.encrypt_message(password, key)

    try:
        conn = sql.connect(con.U_DB)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO user (username, password, pfp_image, relation_foll, relation_following, threads_total, biography) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (username, hashed_password, pfp_image, relation_foll, relation_following, threads_total, biography))
        conn.commit()

        # Ambil user_id baru
        cursor.execute('SELECT last_insert_rowid()')
        user_id = cursor.fetchone()[0]

        flash('Account created successfully!', 'success')
        rec.create_user_action(user_id)
    except sql.Error as e:
        conn.rollback()
        flash('An error occurred while creating the account.', 'error')
    finally:
        conn.close()
