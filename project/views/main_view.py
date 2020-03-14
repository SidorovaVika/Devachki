from flask.views import View
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user
from components.auth import LoginUser
import datetime
from models import db
from models.departments import Department
from models.user_department import UserDepartment
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class MainView(View):
    def dispatch_request(self):
        """szfo = Department(name="СЗФО", parent_id=None, level=1)
        db.session.add(szfo)
        ao = Department(name="Архангельская область", parent_id=1, level=2)
        db.session.add(ao)
        lo = Department(name="Ленинградская область", parent_id=1, level=2)
        db.session.add(lo)
        po = Department(name="Псковская область", parent_id=1, level=2)
        db.session.add(po)
        arh = Department(name="Архангельск", parent_id=2, level=3)
        db.session.add(arh)
        kot = Department(name="Котлас", parent_id=2, level=3)
        db.session.add(kot)
        cd = Department(name="Северодвинск", parent_id=2, level=3)
        db.session.add(cd)
        ti = Department(name="Тихвин", parent_id=3, level=3)
        db.session.add(ti)
        to = Department(name="Тосно", parent_id=3, level=3)
        db.session.add(to)
        lu = Department(name="Луга", parent_id=3, level=3)
        db.session.add(lu)
        pe = Department(name="Печоры", parent_id=4, level=3)
        db.session.add(pe)
        ne = Department(name="Невель", parent_id=4, level=3)
        db.session.add(ne)
        pus = Department(name="Пустошка", parent_id=4, level=3)
        db.session.add(pus)
        db.session.commit()
        user = User(name="Главный", surname="Самый", email="important@mail.ru", phone="+79215729636",
                    password=generate_password_hash("1234"))
        db.session.add(user)
        db.session.commit()
        user_dep_id = UserDepartment(user_id=user.id, department_id=Department.query.filter(
            Department.name == "Тихвин").first().id, post="Руководитель Федерального Отделения",
                                     employment_date=datetime.date.today(), dismissal_date=None)
        db.session.add(user_dep_id)
        db.session.commit()
        login_user(LoginUser(user))"""
        if current_user.is_authenticated:
            return redirect(url_for('user', user_id=current_user.get_id()))
        return render_template('main.html')