from flask.views import View
from flask import render_template
from flask_login import current_user
from models.user import User
from models.departments import Department
from models.user_department import UserDepartment

class UserView(View):
    def dispatch_request(self,user_id):
        user = User.query.filter(User.id == user_id).first()
        dep_id=UserDepartment.query.filter(UserDepartment.user_id==user.id).first().department_id
        dep=Department.query.filter(Department.id == dep_id).first()
        cur_user_id = int(current_user.get_id())
        our_dep_id = UserDepartment.query.filter(UserDepartment.user_id == cur_user_id).first().department_id
        post = UserDepartment.query.filter(UserDepartment.user_id == cur_user_id).first().post
        if post=="Руководитель Федерального Отделения":
            director=True
        else:
            director=False
        return render_template('user.html',user=user,dep=dep,cur_user_id=cur_user_id,our_dep_id=our_dep_id,director=director)