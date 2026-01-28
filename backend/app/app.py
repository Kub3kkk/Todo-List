from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'klucz'



db = SQLAlchemy(app)

