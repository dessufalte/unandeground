import sqlite3 as sql
from flask import session, flash, url_for, redirect,render_template
from config import AppConfig as con
from functions import feature_thread as thread_view
from secure_information import crypt

def login(username,password):
    
    conn = sql.connect(con.U_DB)
    cursor = conn.cursor()
        
    cursor.execute('SELECT username, password FROM user WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    conn.close()
    key = crypt.generate_key()
    if user and crypt.encrypt_message(password,key):
        session['username'] = username  
        return redirect(url_for('dashboard', username=username))  
    else:
        flash('Invalid credentials. Please check your username and password.', 'error')
        return redirect(url_for('login'))

def auth(username):
    conn = sql.connect(con.U_DB)
    cursor = conn.cursor()
        
    cursor.execute('SELECT pfp_image, biography FROM user WHERE username = ?', (username,))
    user_data = cursor.fetchone()
        
    conn.close()
        
    if user_data:
        pfp_image = user_data[0]
        biography = user_data[1]
        threads_with_pfp = thread_view.thread_viewer(1,2)

        dashboard_data = {
            'username': username,
            'pfp_image': pfp_image,
            'biography': biography,
            'threads_with_pfp': threads_with_pfp
        }
        return dashboard_data
    else:
        flash('User data not found.', 'error')
        return redirect(url_for('login'))
    
    