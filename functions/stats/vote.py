import sqlite3 as sql
from config import AppConfig as con
from functions.stats import action as act

def downvote(user_id, thread_id):
    if not act.check_user_action(user_id, 'downvote', thread_id=thread_id):
        act.record_user_action(user_id, 'downvote', thread_id=thread_id)
        increase_downvote(thread_id)
    else:
        act.delete_user_action_exists(user_id, 'downvote', thread_id=thread_id)
        decrease_downvote(thread_id)

def increase_downvote(thread_id):
    try:
        conn = sql.connect(con.T_DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE threads SET downvotes = downvotes + 1 WHERE thread_id = ?', (thread_id,))
        conn.commit()
    except sql.Error as e:
        print('Error:', e)
    finally:
        conn.close()

def decrease_downvote(thread_id):
    try:
        conn = sql.connect(con.T_DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE threads SET downvotes = downvotes - 1 WHERE thread_id = ?', (thread_id,))
        conn.commit()
    except sql.Error as e:
        print('Error:', e)
    finally:
        conn.close()

def increase_upvote(thread_id):
    try:
        conn = sql.connect(con.T_DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE threads SET upvotes = upvotes + 1 WHERE thread_id = ?', (thread_id,))
        conn.commit()
    except sql.Error as e:
        print('Error:', e)
    finally:
        conn.close()

def decrease_upvote(thread_id):
    try:
        conn = sql.connect(con.T_DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE threads SET upvotes = upvotes - 1 WHERE thread_id = ?', (thread_id,))
        conn.commit()
    except sql.Error as e:
        print('Error:', e)
    finally:
        conn.close()


def upvote(user_id, thread_id):
    if act.check_user_action(user_id, 'upvote', thread_id=thread_id):
        act.delete_user_action_exists(user_id, 'upvote', thread_id=thread_id)
        decrease_upvote(thread_id)
    else:
        if act.check_user_action(user_id, 'downvote', thread_id=thread_id):
            act.delete_user_action_exists(user_id, 'downvote', thread_id=thread_id)
            decrease_downvote(thread_id)
        act.record_user_action(user_id, 'upvote', thread_id=thread_id)
        increase_upvote(thread_id)

def downvote(user_id, thread_id):
    if act.check_user_action(user_id, 'downvote', thread_id=thread_id):
        act.delete_user_action_exists(user_id, 'downvote', thread_id=thread_id)
        decrease_downvote(thread_id)
    else:
        if act.check_user_action(user_id, 'upvote', thread_id=thread_id):
            act.delete_user_action_exists(user_id, 'upvote', thread_id=thread_id)
            decrease_upvote(thread_id)
        act.record_user_action(user_id, 'downvote', thread_id=thread_id)
        increase_downvote(thread_id)