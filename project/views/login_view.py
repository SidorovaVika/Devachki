from flask.views import View
from flask import render_template,redirect, url_for, request
from flask_login import login_user, current_user
from models.user import User
from components.auth import LoginUser
from werkzeug.security import generate_password_hash, check_password_hash
from forms.login_form import LoginForm


class LoginView(View):
    def dispatch_request(self):
        if request.method == 'POST':
            form=LoginForm()
            if form.validate_on_submit():
                if check_password_hash(User.query.filter(User.email==form.email.data).first().password,form.password.data):
                    user = LoginUser(User.query.filter(User.email==form.email()).first())
                    login_user(user)
                    return redirect(url_for('local'))
            else:
                return render_template('login.html', form=form)
        return render_template('login.html',indic=current_user.is_authenticated,form=LoginForm())