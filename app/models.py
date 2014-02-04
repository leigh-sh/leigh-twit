from app import db

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(80), index = True, unique = True)
    posts = db.relationship('Posts', backref = 'author', lazy = 'dynamic')
    followed = // TODO
        
        
    def __repr__(self):
        return '<Users %r>' % (self.user_name)    


    def is_authenticated(self):
        return True
        

    def get_id(self):
        return unicode(self.id)
        
	def follow(self, user):
		if not self.is_following(user):
			self.followed.append(user)
			return self
            
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self
            
                   
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.String(200))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<Posts %r>' % (self.tweet)
        
