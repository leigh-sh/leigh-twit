import os, subprocess, sys
subprocess.call(['python', 'virtualenv.py', 'flask'])
bin = 'bin'
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask<0.10'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-login'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'sqlalchemy==0.7.9'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-sqlalchemy'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-wtf'])