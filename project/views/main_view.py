from flask.views import View
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from models import db
from models.departments import Department

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
        db.session.commit()"""
        if current_user.is_authenticated:
            return redirect(url_for('user', user_id=current_user.get_id()))
        return render_template('main.html')