from sqlalchemy import func
from models import db


class Advisor(db.Model):
    __tablename__ = 'advisor'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)
    employment_date=db.Column(db.Date, nullable=True)
    dismissal_date=db.Column(db.Date, nullable=True)
    #__table_args__ = (db.ForeignKeyConstraint(['user_id'], ['user.id'], name='users_tag_maps_department_id_fk'),)