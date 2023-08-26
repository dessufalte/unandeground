from flask import current_app as app
from flask import render_template,url_for,request,session,flash,redirect,Flask
from config import AppConfig as con
from functions import feature_thread as thread
from functions import feature_login as log
from functions import feature_profile as acc
from functions import feature_comment as comment
from functions.stats import vote as vt
from functions.feature_redirect import *

app = Flask(__name__)
app.secret_key = con.SECRET_KEY

#routes

@app.route("/")
@app.route("/home")
def home():
    image_url = url_for(con.STATIC, filename=con.UNANDEGROUND_BACKGROUND)
    return render_template(con.LOGIN_TEMPLATE,image_url=image_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return log.login(username,password)
    return redirect_to_login()

@app.route('/dashboard/<username>')
def dashboard(username):
    if 'username' in session:
        dashboard_data = log.auth(username)
        script_url = url_for(con.STATIC, filename=con.SCRIPT_JS)
        return render_template(con.DASHBOARD_TEMPLATE,**dashboard_data, script_url=script_url)
    else:
        flash('Please log in to access the dashboard.', 'error')
        return redirect_to_login()
    
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if acc.check_existing_username(username):
            flash('Username already exists. Please choose a different username.', 'error')
            return redirect_to_login()

        acc.create_account(username, password)
        return redirect(url_for('dashboard',username=username))
    return redirect_to_login()

@app.route('/create_thread', methods=['POST'])
def create_thread_route():
    if 'username' in session:
        username = session['username']
        thread_content = request.form['thread_content']
        thread.create_thread(thread_content, username)
        return redirect_to_dashboard()
    else:
        flash('Please log in to create a thread.', 'error')
        return redirect_to_login()

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' in session:
        if request.method == 'POST':
            new_username = request.form['username']
            new_password = request.form['password']
            new_bio = request.form['biog']
            if not acc.check_existing_username(new_username):
                acc.update_profile(session['username'], new_username, new_password, new_bio)
                flash('Profile updated successfully!', 'success')
                session['username'] = new_username
            else:
                flash('Username already in use. Please choose a different username.', 'error')
        return redirect_to_dashboard()
    else:
        flash('Please log in to access your profile.', 'error')
        return redirect_to_login()
    
@app.route('/post_comment/<int:thread_id>', methods=['POST'])
def post_comment(thread_id):
    if 'username' in session:
        username = session['username']
        comment_content = request.form['comment_content']
        parent_id = request.form.get('parent_id')
        if parent_id == '' or parent_id is None:
            parent_id = ''
        comment.create_comment(thread_id,username,comment_content,parent_id)
        return redirect_to_dashboard()
    else:
        flash('Please log in to post a comment.', 'error')
        return redirect_to_login()

@app.route('/upvote/<int:thread_id>', methods=['POST'])
def upvote(thread_id):
    if 'username' in session:
        username = session['username']
        user_id = acc.get_id_by_username(username)
        vt.upvote(user_id,thread_id)
        return redirect_to_dashboard()
    else:
        flash('Please log in to upvote', 'error')
        return redirect_to_login()

@app.route('/downvote/<int:thread_id>', methods=['POST'])
def downvote(thread_id):
    if 'username' in session:
        username = session['username']
        user_id = acc.get_id_by_username(username)
        vt.downvote(user_id,thread_id)
        return redirect_to_dashboard()
    else:
        flash('Please log in to downvote', 'error')
        return redirect_to_login()

#filter

@app.template_filter('get_comments')
def filter_comments(thread_id):
    return comment.get_comments(thread_id)

@app.template_filter('get_reply')
def filter_reply(comment_id):
    return comment.get_reply(comment_id)


#session
@app.before_request
def check_valid_session():
    if request.endpoint == 'dashboard' and 'username' not in session:
        flash('Please log in to access this page.', 'error')
        return redirect(url_for('login'))
    
#error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(Exception)
def server_error(e):
    return render_template('error.html'), 500