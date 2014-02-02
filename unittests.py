#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import User, Post

class MyTest(unittest.TestCase):

	TESTING = True
   

	def setUp(self):
		'''sets up a database before each test'''
		db.create_all()
    
    
	def tearDown(self):
		'''removes SQLAlchemy session after each test'''
		db.session.remove()
		db.drop_all()


	def test_login(self, username, password):
		'''tests login function'''
		return self.app.post('/login', data={
		'username': username,
		'password': password
		}, follow_redirects=True)
  
  	
	def test_sign_out(self):
		'''tests sign_out function'''
		return self.app.get('/signout', follow_redirects=True)    
        
          
if __name__ == '__main__':
	unittest.main()
