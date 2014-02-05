from app import db

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(80), index = True, unique = True)
    posts = db.relationship('Posts', backref = 'users', lazy = 'dynamic')
    followed = db.relationship('Users', 
        secondary = followers, 
        primaryjoin = (followers.c.follower_id == id), 
        secondaryjoin = (followers.c.followed_id == id), 
        backref = db.backref('followers', lazy = 'dynamic'), 
        lazy = 'dynamic')

 
    def __repr__(self):
        return '<Users %r>' % (self.user_name)    


    def is_authenticated(self):
        return True
        
    def is_active(self):
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
            
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        return Posts.query.join(followers, 
    (followers.c.followed_id == Posts.user_id)).filter(followers.c.follower_id == self.id)
     
       
    @staticmethod    
    def create_unique_username(user_name):
        count = 0
        user_name += str(count)
        if Users.query.filter_by(user_name = user_name).first() == None:
            return user_name
        while True:
            user_name +=str(count)
            if Users.query.filter_by(user_name = unique_user_name).first() == None:
	            break
            count += 1	    
            return user_name	
            
                             
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<Posts %r>' % (self.tweet)
        
        
        