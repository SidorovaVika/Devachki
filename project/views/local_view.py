from flask.views import View
from flask import render_template, request
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department


class LocalView(View):
    def dispatch_request(self,dep_id):
        dep=Department.query.filter(Department.id==dep_id).first()
        users=User.query.filter(User.department==dep.name).all()
        parent=Department.query.filter(Department.name==dep.parent).first()
        user_id=current_user.get_id()
        return render_template('local.html',user_id=user_id,users=users,parent=parent,dep=dep)