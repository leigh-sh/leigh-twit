from flask import render_template, flash, redirect, g, session, request
from flask.ext.login import login_manager
from app import app,login_manager


@login_manager.user_loader
def load_user(id):
	'''Login manager. Reloads the user from the database'''
    return User.query.get(int(id)) ## conversion to int, flask-login accepts userid as int


@app.before_request
def before_request():
    '''is called before a request'''
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

def internal_error(error):
	'''Error handler'''
	db.session.rollback()
	return render_template('500.html'), 500
