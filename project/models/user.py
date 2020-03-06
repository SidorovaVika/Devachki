from sqlalchemy import func
from models import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(200), nullable=False)
    surname = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(200), nullable=False, unique=True)
    phone = db.Column(db.VARCHAR(200), nullable=False)
    password = db.Column(db.VARCHAR(200), nullable=False)