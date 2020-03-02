from flask.views import View
from flask import render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department
import datetime
from models import db


class ChangeView(View):


    def dispatch_request(self, user_id, var):
        user=User.query.filter(User.id==current_user.get_id()).first()
        role = user.get_role()
        user_loc_dep=UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().department_id
        user_reg_dep=Department.query.filter(Department.id==user_loc_dep).first().parent_id
        chil=Department.query.filter(Department.parent_id==user_reg_dep).all()
        chil_id=[i.id for i in chil]

        if var=='add_staff':
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
            return redirect(url_for('add_staff'))




        if var=='add_federal_zam':
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().post=="Заместитель Руководителя Федерального Отделения":
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




        if var=='add_regional_director':
            if UserDepartment.query.filter(UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().post == "Руководитель Регионального Отделения":
                flash("Данный сотрудник уже на этой должности")
            elif UserDepartment.query.filter(
                    UserDepartment.post == "Руководитель Регионального Отделения").filter(UserDepartment.department_id.in_(chil_id)).filter(
                    UserDepartment.dismissal_date == None).first():
                flash("Данная вакансия недоступна")
            else:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Руководитель Регионального Отделения",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")




        if var=='add_regional_zam':
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().post=="Заместитель Руководителя Регионального Отделения":
                flash("Данный сотрудник уже на этой должности")
            elif len(UserDepartment.query.filter(UserDepartment.post=="Заместитель Руководителя Регионального Отделения").filter(UserDepartment.department_id.in_(chil_id)).filter(UserDepartment.dismissal_date == None).all())<3:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Регионального Отделения",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")
            else:
                flash("Данная вакансия недоступна")




        if var=='add_local_director':
            if UserDepartment.query.filter(UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().post == "Руководитель Местного Отделения":
                flash("Данный сотрудник уже на этой должности")
            elif UserDepartment.query.filter(
                    UserDepartment.post == "Руководитель Местного Отделения").filter(UserDepartment.department_id==user_loc_dep).filter(
                    UserDepartment.dismissal_date == None).first():
                flash("Данная вакансия недоступна")
            else:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Руководитель Местного Отделения",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")




        if var=='add_local_zam':
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().post=="Заместитель Руководителя Местного Отделения":
                flash("Данный сотрудник уже на этой должности")
            elif len(UserDepartment.query.filter(UserDepartment.post=="Заместитель Руководителя Местного Отделения").filter(UserDepartment.department_id==user_loc_dep).filter(UserDepartment.dismissal_date == None).all())<3:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Заместитель Руководителя Местного Отделения",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")
            else:
                flash("Данная вакансия недоступна")




        if var=='dis_staff':
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().post=="Пользователь":
                flash("Данный пользователь не является сотрудником")
            else:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Пользователь",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")





        if var=='staff':
            if UserDepartment.query.filter(UserDepartment.user_id==user_id).filter(UserDepartment.dismissal_date == None).first().post=="Сотрудник":
                flash("Данный сотрудник уже на этой должности")
            else:
                UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).filter(
                    UserDepartment.dismissal_date == None).first().dismissal_date = datetime.date.today()
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == user_id).first().department_id, post="Сотрудник",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                db.session.add(user_dep_id)
                db.session.commit()
                flash("Успешно")

        return redirect(url_for('user',user_id=user_id))

    """def dispatch_request(self, users, var):
            users_id=[i.id for i in users]
            if var == 'add_all_staff':
                users_deps=UserDepartment.query.filter(
                    UserDepartment.user_id.in_(users_id)).all()
                for i in users_deps:
                    i.dismissal_date = datetime.date.today()
                    db.session.commit()
                    user_dep_id = UserDepartment(user_id=i.user_id, department_id=UserDepartment.query.filter(
                    UserDepartment.user_id == i.user_id).first().department_id, post="Сотрудник",
                                             employment_date=datetime.date.today(), dismissal_date=None)
                    db.session.add(user_dep_id)
                    db.session.commit()
                users = User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
                    UserDepartment.dismissal_date.is_(None)).all()
                user_id = current_user.get_id()
                flash("Успешно")
                return render_template('add_staff.html', users=users, user_id=user_id)"""