from flask import render_template, flash, redirect, g, session, request
from flask.ext.login import current_user, login_user, logout_user
from app import app, login_manager

@login_manager.user_loader
def load_user(id):
	'''Callback. Reloads the user from the database'''
	return User.query.get(int(id)) ## conversion to int, flask-login accepts userid as int


@app.before_request
def before_request():
	'''called before a request'''
	g.user = current_user
	if session['user_id']:
		g.user = query_db('select * from Users where user_id = ?',
                session['user_id'], one=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
	'''Displays the login page'''
	if g.user:
		return redirect(url_for('timeline'))
	error = None
	
	
@app.route('/signout')
def sign_out():
    '''Signs the user out'''
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
