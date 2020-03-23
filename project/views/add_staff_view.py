from flask.views import View
from flask import render_template
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department
import random


class AddStaffView(View):
    def dispatch_request(self):
        user_id = current_user.get_id()
        loc_dep = UserDepartment.query.filter(UserDepartment.user_id == user_id).first().department_id
        reg_dep = Department.query.filter(Department.id == loc_dep).first().parent_id
        chil = Department.query.filter(Department.parent_id == reg_dep).all()
        chil_id = [i.id for i in chil]
        post = UserDepartment.query.filter(UserDepartment.user_id == user_id).filter(
            UserDepartment.dismissal_date == None).first().post
        if post == 'Руководитель Местного Отделения' or post == 'Заместитель Руководителя Местного Отделения':
            users = User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
                UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.department_id == loc_dep).all()
        if post == 'Руководитель Регионального Отделения' or post == 'Заместитель Руководителя Регионального Отделения':
            users = User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
                UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.department_id.in_(chil_id)).all()
        if post == 'Руководитель Федерального Отделения' or post == 'Заместитель Руководителя Федерального Отделения':
            users = User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
                UserDepartment.dismissal_date.is_(None)).all()
        random.shuffle(users)
        return render_template('add_staff.html', users=users, user_id=user_id)
