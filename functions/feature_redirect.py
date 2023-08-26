from flask import redirect,session,url_for

def redirect_to_dashboard():
    if 'username' in session:
        username = session['username']
        return redirect(url_for('dashboard', username=username))
    else:
        return redirect_to_login() 
     
def redirect_to_login():
    return redirect(url_for('home'))