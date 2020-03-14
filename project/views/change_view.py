from flask.views import View
from flask import render_template, request, redirect, url_for
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department
import datetime
from models import db


class ChangeView(View):
    def dispatch_request(self,user_id,var):
        if var==7:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().dismissal_date=datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Сотрудник",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
            users = User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
                UserDepartment.dismissal_date.is_(None)).all()
            user_id = current_user.get_id()
            return render_template('add_staff.html', users=users, user_id=user_id)
        if var==1:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Федерального Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==2:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Руководитель Регионального Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==3:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Регионального Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==4:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Руководитель Местного Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==5:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Местного Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==6:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Пользователь",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==0:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id and UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Сотрудник",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        return redirect(url_for('user',user_id=user_id))

