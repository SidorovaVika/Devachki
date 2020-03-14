from flask.views import View
from flask import render_template, request
from models.user import User
from flask_login import current_user
from models.user_department import UserDepartment
from models.departments import Department


class LocalView(View):
    def dispatch_request(self, dep_id):
        dep=Department.query.filter(Department.id==dep_id).first()
        staff = User.query.join(User.user_departments).filter(UserDepartment.department_id==dep_id).filter(UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.post=="Сотрудник").all()
        parent=Department.query.filter(Department.id==dep.parent_id).first()
        user_id=current_user.get_id()
        loc_dir=User.query.join(User.user_departments).filter(UserDepartment.department_id==dep_id).filter(UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.post=="Руководитель Местного Отделения").first()
        loc_zam=User.query.join(User.user_departments).filter(UserDepartment.department_id==dep_id).filter(UserDepartment.dismissal_date.is_(None)).filter(UserDepartment.post=="Заместитель Руководителя Местного Отделения").all()
        return render_template('local.html',user_id=user_id,staff=staff,parent=parent,dep=dep,loc_dir=loc_dir,loc_zam=loc_zam)