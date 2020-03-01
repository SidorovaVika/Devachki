from flask.views import View
from flask import render_template,request
from models.departments import Department
from flask_login import current_user

class RegionalView(View):
    def dispatch_request(self,parent_id):
        dep = Department.query.filter(Department.id == parent_id).first()
        chil=Department.query.filter(Department.parent == dep.name).all()
        par_name = Department.query.filter(Department.name == dep.parent).first().name
        parent = Department.query.filter(Department.name == par_name).first()
        return render_template('regional.html',chil=chil,parent=parent,user_id=current_user.get_id())