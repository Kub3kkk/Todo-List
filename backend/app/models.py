from extensions import db

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(100), unique=True, nullable=False)
    password = db.column(db.String(200), nullable=False)