from flask.views import View
from flask import render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department
import datetime
from models import db


class ChangeView(View):

    actions = {
        'add_federal_zam': (
            'Назначить заместителем руководителя федерального отделения', ['Руководитель Федерального Отделения']),
        'add_regional_director': (
            'Назначить руководителем регионального отделения', ['Руководитель Федерального Отделения','Заместитель Руководителя Федерального Отделения']),
        'add_regional_zam': (
            'Назначить заместителем руководителя регионального отделения', ['Руководитель Регионального Отделения']),
        'add_local_director': (
            'Назначить руководителем местного отделения', ['Руководитель Федерального Отделения','Заместитель Руководителя Федерального Отделения','Руководитель Регионального Отделения','Заместитель Руководителя Регионального Отделения']),
        'add_local_zam': (
        'Назначить заместителем руководителя местного отделения', ['Руководитель Местного Отделения']),
        'add_staff': (
            'Принять на работу', ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
             'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения',
                                  'Руководитель Местного Отделения', 'Заместитель Руководителя Местного Отделения']),
        'dis_federal_zam': (
            'Уволить', ['Руководитель Федерального Отделения']),
        'dis_regional_director': (
            'Уволить',
            ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения']),
        'dis_regional_zam': (
            'Уволить', ['Руководитель Регионального Отделения']),
        'dis_local_director': (
            'Уволить',
            ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
             'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения']),
        'dis_local_zam': (
            'Уволить', ['Руководитель Местного Отделения']),
        'dis_staff': (
            'Уволить',
            ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
             'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения',
             'Руководитель Местного Отделения', 'Заместитель Руководителя Местного Отделения']),
    }

    def dispatch_request(self, user_id, var):

        role = get_role(current_user)
        if var not in self.actions:
            pass

        if role not in self.actions[var][1]:
            pass

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
            flash("Успешно")
            return render_template('add_staff.html', users=users, user_id=user_id)
        if var==1:
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).first().post=="Заместитель Руководителя Федерального Отделения":
                flash("Данный сотрудник уже на этой должности")
            elif len(UserDepartment.query.filter(UserDepartment.post=="Заместитель Руководителя Федерального Отделения").filter(UserDepartment.dismissal_date == None).all())<3:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Федерального Отделения",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")
            else:
                flash("Данная вакансия недоступна")

        if var==2:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(
                UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Руководитель Регионального Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==3:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(
                UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Регионального Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==4:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(
                UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Руководитель Местного Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==5:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Местного Отделения",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==6:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(
                UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Пользователь",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        if var==0:
            UserDepartment.query.filter(
                UserDepartment.user_id == user_id).filter(
                UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
            db.session.commit()
            user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                UserDepartment.user_id == user_id).first().department_id, post="Сотрудник",
                                         employment_date=datetime.date.today(), dismissal_date=None)
            db.session.add(user_dep_id)
            db.session.commit()
        return redirect(url_for('user',user_id=user_id))

