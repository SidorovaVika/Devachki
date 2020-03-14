from flask.views import View
from flask import render_template
from models.departments import Department
from flask_login import current_user
from models.user_department import UserDepartment
from models.user import User

class FederalView(View):
    def dispatch_request(self,dep_id):
        dep=Department.query.filter(Department.id == dep_id).first()
        chil = Department.query.filter(Department.parent_id == dep_id).all()
        chil_id=[]
        chil_chil=[]
        for i in chil:
            children=Department.query.filter(Department.parent_id == i.id).all()
            chil_id.append([j.id for j in children])
        for i in range(len(chil_id)):
            chil_chil.append([])
            for j in chil_id[i]:
                chil_chil[i].append(len(User.query.join(User.user_departments).filter(UserDepartment.department_id == j).filter(
                        UserDepartment.dismissal_date.is_(None)).all()))
        for i in range(len(chil_chil)):
            chil_chil[i]=sum(chil_chil[i])
        director=User.query.join(User.user_departments).filter(UserDepartment.post == "Руководитель Федерального Отделения").filter(
            UserDepartment.dismissal_date.is_(None)).first()
        fed_zam = User.query.join(User.user_departments).filter(
            UserDepartment.dismissal_date.is_(None)).filter(
            UserDepartment.post == "Заместитель Руководителя Федерального Отделения").all()
        return render_template('federal.html',chil=chil,user_id=current_user.get_id(),dep=dep,chil_chil=chil_chil,director=director,fed_zam=fed_zam)