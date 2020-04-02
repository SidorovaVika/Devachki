from flask.views import View
from flask import render_template
from project.models.departments import Department
from flask_login import current_user
from project.models.user import User
from project.models.user_department import UserDepartment
from sqlalchemy import func
from project.models import db
from project.models.advisory_board import Advisor


class RegionalView(View):
    def dispatch_request(self, dep_id):
        dep = Department.query.filter(Department.id == dep_id).first()
        chil = Department.query.filter(Department.parent_id == dep_id).all()
        count_users = db.session.query(
            UserDepartment.department_id,
            func.count('*').label('c_count')
        ).filter(
            UserDepartment.department_id.in_([i.id for i in chil])
        ).filter(
            UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.post != "Пользователь").group_by(
            UserDepartment.department_id).all()
        count_users = dict(count_users)
        parent = Department.query.filter(Department.id == dep.parent_id).first()
        reg_dir = User.query.join(User.user_departments).filter(
            UserDepartment.department_id.in_([i.id for i in chil])).filter(
            UserDepartment.dismissal_date.is_(None)).filter(
            UserDepartment.post == "Руководитель Регионального Отделения").first()
        reg_zam = User.query.join(User.user_departments).filter(
            UserDepartment.department_id.in_([i.id for i in chil])).filter(
            UserDepartment.dismissal_date.is_(None)).filter(
            UserDepartment.post == "Заместитель Руководителя Регионального Отделения").all()
        advis_id = [i.user_id for i in
                    Advisor.query.filter(Advisor.department_id == dep_id).filter(Advisor.dismissal_date == None).all()]
        advisors = User.query.filter(User.id.in_(advis_id)).all()
        return render_template('regional.html', chil=chil, parent=parent, user_id=current_user.get_id(), dep=dep,
                               count_users=count_users, reg_dir=reg_dir, reg_zam=reg_zam, advisors=advisors)
