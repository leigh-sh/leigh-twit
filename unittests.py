
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
        
          
if __name__ == '__main__':
	unittest.main()
