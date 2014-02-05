#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db, SQLALCHEMY_DATABASE_URI
from app.models import User, Post

class MyTest(unittest.TestCase):

	TESTING = True
   

	def setUp(self):
		'''sets up a database before each test'''
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		db.create_all()
    
    
	def tearDown(self):
		'''removes SQLAlchemy session after each test'''
		db.session.remove()
		db.drop_all()

	
	def test_login(self, username, password):
		'''tests login function'''
		tester = app.test_client(self)
		response = tester('/login', content_type='html/text')
		self.assertEqual(response.status_code,200)
  
  	
	def test_sign_out(self):
		'''tests sign_out function'''
		tester = app.test_client(self)
		response = tester('/signout', content_type='html/text')
		self.assertEqual(response.status_code,200)
		
		
    def create_unique_username(self):
        leigh = User(user_name = 'leigh')
        db.session.add(leigh)
        db.session.commit()
        username = User.create_unique_username('leigh')
        assert nickname != 'leigh'

        leigh = User(user_name = username)
        db.session.add(leigh)
        db.session.commit()
        another_username = User.create_unique_username('leigh')
        assert another_username != 'leigh'
        assert another_username != username
        
    def test_follow(self):
        leigh = User(user_name = 'leigh')
        shaniv = User(user_name = 'shaniv')
        db.session.add(leigh)
        db.session.add(shaniv)
        db.session.commit()
        assert leigh.unfollow(shaniv) == None
        test_user = leigh.follow(shaniv)
        db.session.add(test_user)
        db.session.commit()
        assert leigh.follow(shaniv) == None
        assert leigh.is_following(shaniv)
        assert leigh.followed.count() == 1
        assert leigh.followed.first().user_name == 'shaniv'
        assert shaniv.followers.count() == 1
        assert shaniv.followers.first().user_name == 'leigh'
        test_user = leigh.unfollow(shaniv)
        assert test_user != None
        db.session.add(test_user)
        db.session.commit()
        assert leigh.is_following(shaniv) == False
        assert leigh.followed.count() == 0
        assert shaniv.followers.count() == 0  
               
if __name__ == '__main__':
	unittest.main()