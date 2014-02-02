from flask import render_template, flash, redirect, g, session, request
from flask.ext.login import login_user
from app import app,lm
from forms import LoginForm


@lm.user_loader
def load_user(id):
	'''Login manager. Reloads the user from the database'''
    return User.query.get(int(id)) ## conversion to int, flask-login accepts userid as int


@app.before_request
def before_request():
    '''is called before a request
    g.user = current_user
    if 'user_id' in session:
        g.user = query_db('select * from Users where user_id = ?',
                          [session['user_id']], one=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Displays the login page""" 
	if g.user:
		return redirect(url_for('timeline'))
	error = None
	if request.method == 'POST':
		user = query_db('''select * from user where
			username = ?''', [request.form['username']], one=True)
		if user is None:
			error = 'Invalid username'
		elif not check_password_hash(user['pw_hash'],
                                     request.form['password']):
			error = 'Invalid password'
		else:
			flash('You were logged in')
			session['user_id'] = user['user_id']
            
			return redirect(url_for('timeline'))
            
	return render_template('login.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Registers the user"""
    if g.user:
    
        return redirect(url_for('timeline'))
        
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'Please enter a username'
        elif not request.form['password']:
            error = 'Please enter a password'
        else:
            db = get_db()
            db.execute('''insert into Users (
              username, pw_hash) values (?, ?, ?)''',
              [request.form['username'],
               generate_password_hash(request.form['password'])])
            db.commit()
            flash('Registered successfully')
            
            return redirect(url_for('login'))
    return render_template('login.html', error=error)


@app.route('/signout')
def sign_out():
    """Signs the user out"""
    flash('You were signed out')
    session.pop('user_id', None)
    
    return redirect(url_for('global_feed'))
    
##Decorators to handle errors 
@app.errorhandler(404)
def internal_error(error):
	'''Error handler'''
	return render_template('404.html'), 404

@app.errorhandler(500)
