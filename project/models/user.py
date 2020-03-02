from sqlalchemy import func
from models import db
from models.user_department import UserDepartment

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(200), nullable=False)
    surname = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(200), nullable=False, unique=True)
    phone = db.Column(db.VARCHAR(200), nullable=False)
    password = db.Column(db.VARCHAR(200), nullable=False)

    user_departments = db.relationship('UserDepartment')


    def get_role(self):
        return User.query.join(User.user_departments).filter(
            UserDepartment.user_id==self.id).first().post