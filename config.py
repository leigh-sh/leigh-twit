import os
basedir = os.path.abspath(os.path.dirname(__file__))

##The database URI that will be used for the connection    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
