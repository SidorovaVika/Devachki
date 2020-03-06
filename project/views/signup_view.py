from flask.views import View
from flask import render_template, request
from models import db
from flask_login import current_user, login_user
from models.user import User
from components.auth import LoginUser
from werkzeug.security import generate_password_hash, check_password_hash
from forms.signup_form import SignupForm

class SignupView(View):
    def dispatch_request(self):
        if request.method=='POST':
            form=SignupForm()
            if form.validate_on_submit():
                user=User(name=form.name(),surname=form.surname(),email=form.email(),phone=form.phone(),password=generate_password_hash(form.password()))
                db.session.add(user)
                db.session.commit()
                login_user(LoginUser(user))
            else:
                return render_template('signup.html',form=form)
            return render_template('main.html', indic=current_user.is_authenticated,form=form)
        return render_template('signup.html', indic=current_user.is_authenticated,form=SignupForm())