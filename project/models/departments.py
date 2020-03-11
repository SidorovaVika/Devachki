from sqlalchemy import func
from models import db

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(200), nullable=False)
    parent = db.Column(db.VARCHAR(200), nullable=True)
    level = db.Column(db.Integer, nullable=False)


