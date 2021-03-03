from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.secret_key = '2468'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter-clone1.sqlite3'
db = SQLAlchemy(app)

from flaskr import route
