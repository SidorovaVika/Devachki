from project.models import db


class Advisor(db.Model):
    __tablename__ = 'advisor'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=True)
    employment_date=db.Column(db.Date, nullable=True)
    dismissal_date=db.Column(db.Date, nullable=True)