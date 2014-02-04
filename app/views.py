from flask import render_template, redirect, g, session, request, url_for
from flask.ext.login import current_user, login_user, logout_user, login_required
from app import app, login_manager, db
from forms import LoginForm
from models import User


@login_manager.user_loader
def load_user(id):
	'''Callback. Reloads the user from the database'''
	return User.query.get(int(id)) ## conversion to int, flask-login accepts userid as int


@app.before_request
def before_request():
	'''called before the view function for each request'''
	g.user = current_user

@app.route('/')
@login_required
def global_feed():
	user = g.user
	print 'in global, g.user: %s' % g.user    
	posts = [
        { 
            //TODO 
        },
        { 
            //TODO
        }
    ]
	return render_template('home.html', 
	title = 'Home', 
	user = g.user, 
	posts = posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	'''Displays the login page'''
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('global_feed'))
	form = LoginForm(request.form)
	if form.validate_on_submit():
		//TODO
	else:
		//TODO
	return render_template('login.html', 
        title = 'Login',
        form = form)


	
@app.route('/signout')
def sign_out():
    '''Signs the user out'''
    flash('You were signed out')
    logout_user()
    return redirect(url_for('home'))
    
    
##Decorators to handle errors 
@app.errorhandler(404)
def internal_error(error):
	'''Error handler'''
	return render_template('404.html'), 404

def internal_error(error):
	'''Error handler'''
	db.session.rollback()
	return render_template('500.html'), 500
