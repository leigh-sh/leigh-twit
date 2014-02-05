from flask.ext.wtf import Form
from app.models import Users
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from flask import request, flash


class LoginForm(Form):
     
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
class RegisterForm(Form): 
     
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
          
    def validate(self):
        if request.form["user_name"] is None or request.form["user_name"].strip()=="":
            return False
        inserted_username = request.form["user_name"]
        user = Users.query.filter_by(user_name = inserted_username).first()
        if user != None:
            suggested_username = Users.create_unique_username(inserted_username)
            flash('This username already exists. Consider register with %s' % suggested_username)
            return False
        return True

            
class PostForm(Form):
     
     def __init__(self, *args, **kwargs): 
        Form.__init__(self, *args, **kwargs)