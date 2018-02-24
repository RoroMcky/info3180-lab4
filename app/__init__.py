from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'
UPLOAD_FOLDER = "./app/static/uploads"

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views

#app = Flask(__name__)
#app.config['SECRET_KEY']='Sup3r$3cretkey'
#app.config['SQLALCHEMY_DATABASE_URI']="./app/static/uploads"
#db = SQLAlchemy(app)

DEBUG=True
SECRET_KEY = 'Sup3r$3cretkey'
 
from app import views
