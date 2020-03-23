from flask.views import View
from flask import render_template,redirect, url_for, request
from flask_login import login_user, current_user
from models.user import User
from components.auth import LoginUser
from werkzeug.security import check_password_hash
from forms.login_form import LoginForm
from models.user_department import UserDepartment


class LoginView(View):
    def dispatch_request(self):
        error=None
        if request.method == 'POST':
            form=LoginForm()
            if form.validate_on_submit():
                if check_password_hash(User.query.filter(User.email==form.email.data).first().password,form.password.data):
                    user = LoginUser(User.query.filter(User.email==form.email.data).first())
                    login_user(user)
                    user_id = current_user.get_id()
                    dep_id = UserDepartment.query.filter(UserDepartment.user_id == user_id).first().department_id
                    return redirect(url_for('local',dep_id=dep_id))
                else:
                    return render_template('login.html', form=form,error="Неверный пароль")
            else:
                return render_template('login.html', form=form,error=error)
        return render_template('login.html', form=LoginForm(), error=error)