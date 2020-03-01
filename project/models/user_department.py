from sqlalchemy import func
from models import db


class UserDepartment(db.Model):
    __tablename__ = 'user_department'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
