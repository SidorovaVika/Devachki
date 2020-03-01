from flask.views import View
from flask import render_template
from models.departments import Department
from flask_login import current_user

class FederalView(View):
    def dispatch_request(self,parent_id):
        dep = Department.query.filter(Department.id == parent_id).first()
        chil = Department.query.filter(Department.parent == dep.name).all()
        return render_template('federal.html',chil=chil,user_id=current_user.get_id())