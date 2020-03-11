from flask.views import View
from flask import render_template, request,redirect,url_for
from models import db
from flask_login import current_user, login_user
from models.user import User
from models.departments import Department
from models.user_department import UserDepartment
from components.auth import LoginUser
from werkzeug.security import generate_password_hash, check_password_hash
from forms.signup_form import SignupForm

class SignupView(View):
    def dispatch_request(self):
        if request.method=='POST':
            form=SignupForm()
            if form.validate_on_submit():
                user=User(name=form.name.data,surname=form.surname.data,email=form.email.data,phone=form.phone.data,department=form.department.data,password=generate_password_hash(form.password.data))
                db.session.add(user)
                db.session.commit()
                user_dep_id = UserDepartment(user_id=user.id, department_id=Department.query.filter(Department.name == user.department).first().id)
                db.session.add(user_dep_id)
                db.session.commit()
                login_user(LoginUser(user))
            else:
                return render_template('signup.html',form=form)
            return redirect(url_for('user', user_id=user.id))
        return render_template('signup.html', indic=current_user.is_authenticated,form=SignupForm())