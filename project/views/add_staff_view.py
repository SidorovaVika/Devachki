from flask.views import View
from flask import render_template, request
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department


class AddStaffView(View):
    def dispatch_request(self):
        users=User.query.join(User.user_departments).filter(UserDepartment.post == "Пользователь").filter(
            UserDepartment.dismissal_date.is_(None)).all()
        user_id=current_user.get_id()
        return render_template('add_staff.html',users=users,user_id=user_id)