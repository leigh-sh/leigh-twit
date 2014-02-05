from flask import render_template, flash, redirect, g, session, request, url_for
from flask.ext.login import current_user, login_user, logout_user, login_required
from app import app, login_manager, db
from forms import LoginForm, RegisterForm, PostForm
from models import Users, Posts


@login_manager.user_loader
def load_user(id):
    '''Callback. Reloads the user from the database'''
    return Users.query.get(int(id))
    #conversion to int, flask-login accepts userid as int


@app.before_request
def before_request():
    '''called before the view function for each request'''
    g.user = current_user
    if g.user.is_authenticated():  # if there is a logged in user
        db.session.add(g.user)
        db.session.commit()


@app.route('/feed')
@login_required
def feed():
    if not g.user:
        return redirect(url_for('global_feed'))
    posts = []      # TODO
    return render_template('feed.html', title='Feed', user=g.user, posts=posts)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('profile'))
	form = LoginForm(request.form)
	if form.validate_on_submit():  # if the data is valid
		username=request.form["user_name"]
        user=Users.query.filter_by(user_name=username).first()
        if user is None:
		    user=Users(user_name=username)
		    db.session.add(user)
		    db.session.commit()
        login_user(user)
        posts=user.followed_posts().all()
        return render_template("profile.html", user=user, posts=posts)
		
	return render_template("login.html", form=form)


@app.route('/profile')
@login_required
def profile():    
    form=PostForm(request.form)
    if form.validate_on_submit():
        post=Post(post=form.post.data, user_id=g.user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('profile'))
    posts = g.user.followed_posts()
    return render_template("profile.html", user=g.user, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit() and request.method == 'POST':
        username = request.form["user_name"]
        user = Users(user_name = username)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        flash('Registeration is completed')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/globalfeed')
def global_feed():
	#posts = db.engine.execute('''
    #   select post.*, user_id.* from posts
    #  where posts.user_id = users.user_id''')
    return render_template('feed.html', user = user, posts = posts)


@app.route('/signout')
def sign_out():
    '''Signs the user out'''
    flash('You were signed out')
    logout_user()
    return redirect(url_for('login'))
 
 
@app.route('/follow/<user_name>')
@login_required
def follow(user_name):
    user=User.query.filter_by(user_name=user_name).first()
    if user is None:
        return redirect(url_for('profile'))
    follower = g.user.follow(user)
    #if follower is None:
      # TODO
    db.session.add(follower)
    db.session.commit()
    return  # TODO


@app.route('/unfollow/<user_name>')
@login_required
def unfollow(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    # TODO ERROR if user is None
    unfollower = g.user.unfollow(user)
    if unfollower is None:
        return  # TODO
    db.session.add(unfollower)
    db.session.commit()
    #return /TODO


'''Decorators to handle errors '''


@app.errorhandler(404)
def internal_error(error):
    '''Error handler'''
    return render_template('404.html'), 404


def internal_error(error):
    '''Error handler'''
    db.session.rollback()
    return render_template('500.html'), 500
