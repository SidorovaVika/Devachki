from flask.views import View
from flask import render_template
from flask_login import current_user
from models.user import User
from models.advisory_board import Advisor
from models.departments import Department
from models.user_department import UserDepartment


class UserView(View):
    def dispatch_request(self, user_id):
        main_dep_id=None
        actions = {
            'add_federal_zam': (
                'Назначить заместителем руководителя федерального отделения', ['Руководитель Федерального Отделения']),
            'add_regional_director': (
                'Назначить руководителем регионального отделения',
                ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения']),
            'add_regional_zam': (
                'Назначить заместителем руководителя регионального отделения',
                ['Руководитель Регионального Отделения']),
            'add_local_director': (
                'Назначить руководителем местного отделения',
                ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
                 'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения']),
            'add_local_zam': (
                'Назначить заместителем руководителя местного отделения', ['Руководитель Местного Отделения']),
            'staff': (
                'Назначить сотрудником местного отделения',
                ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
                 'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения',
                 'Руководитель Местного Отделения', 'Заместитель Руководителя Местного Отделения']),
            'dis_staff': (
                'Уволить',
                ['Руководитель Федерального Отделения', 'Заместитель Руководителя Федерального Отделения',
                 'Руководитель Регионального Отделения', 'Заместитель Руководителя Регионального Отделения',
                 'Руководитель Местного Отделения', 'Заместитель Руководителя Местного Отделения'])
        }
        user = User.query.filter(User.id == user_id).first()
        if not (current_user.is_authenticated):
            return render_template('user.html', user=user)

        user_posts = UserDepartment.query.filter(UserDepartment.user_id == user_id).all()
        dep_id = UserDepartment.query.filter(UserDepartment.user_id == user.id).first().department_id
        dep = Department.query.filter(Department.id == dep_id).first()
        user_regional_dep_id = dep.parent_id
        cur_user_id = int(current_user.get_id())
        our_dep_id = UserDepartment.query.filter(UserDepartment.user_id == cur_user_id).first().department_id
        our_dep = Department.query.filter(Department.id == our_dep_id).first()
        our_regional_dep_id = our_dep.parent_id
        post = UserDepartment.query.filter(UserDepartment.user_id == cur_user_id).filter(
            UserDepartment.dismissal_date == None).first().post
        opportunities = []
        for i in actions:
            if post in actions[i][1]:
                opportunities.append(i)
        regional_indic = user_regional_dep_id == our_regional_dep_id
        local_indic = dep_id == our_dep_id
        dis_indic = False
        user_post = UserDepartment.query.filter(UserDepartment.user_id == user_id).filter(
            UserDepartment.dismissal_date == None).first().post

        if post == 'Руководитель Федерального Отделения':
            if user_post == 'Заместитель Руководителя Федерального Отделения' or user_post == 'Руководитель Регионального Отделения' or user_post == 'Заместитель Руководителя Регионального Отделения' or user_post == 'Руководитель Местного Отделения' or user_post == 'Заместитель Руководителя Местного Отделения' or user_post == 'Сотрудник' or user_post == 'Пользователь':
                dis_indic = True

        if post == 'Заместитель Руководителя Федерального Отделения':
            if user_post == 'Руководитель Регионального Отделения' or user_post == 'Заместитель Руководителя Регионального Отделения' or user_post == 'Руководитель Местного Отделения' or user_post == 'Заместитель Руководителя Местного Отделения' or user_post == 'Сотрудник' or user_post == 'Пользователь':
                dis_indic = True

        if post == 'Руководитель Регионального Отделения':
            if regional_indic:
                if user_post == 'Заместитель Руководителя Регионального Отделения' or user_post == 'Руководитель Местного Отделения' or user_post == 'Заместитель Руководителя Местного Отделения' or user_post == 'Сотрудник' or user_post == 'Пользователь':
                    dis_indic = True

        if post == 'Заместитель Руководителя Регионального Отделения':
            if regional_indic:
                if user_post == 'Руководитель Местного Отделения' or user_post == 'Заместитель Руководителя Местного Отделения' or user_post == 'Сотрудник' or user_post == 'Пользователь':
                    dis_indic = True

        if post == 'Руководитель Местного Отделения':
            if local_indic:
                if user_post == 'Заместитель Руководителя Местного Отделения' or user_post == 'Сотрудник' or user_post == 'Пользователь':
                    dis_indic = True

        if post == 'Заместитель Руководителя Местного Отделения':
            if local_indic:
                if user_post == 'Сотрудник' or user_post == 'Пользователь':
                    dis_indic = True

        if post == "Руководитель Федерального Отделения":
            main_dep_id = 1
        if post == "Руководитель Регионального Отделения":
            main_dep_id = Department.query.filter(Department.id == UserDepartment.query.filter(
                UserDepartment.user_id == user.id).first().department_id).first().parent_id
        if post == "Руководитель Местного Отделения":
            main_dep_id = UserDepartment.query.filter(UserDepartment.user_id == user.id).first().department_id

        advisor_indic = Advisor.query.filter(Advisor.user_id == user_id).filter(Advisor.dismissal_date == None).filter(
            Advisor.department_id == main_dep_id).first()

        return render_template('user.html', user=user, dep=dep, cur_user_id=cur_user_id, local_indic=local_indic,
                               opportunities=opportunities, actions=actions, regional_indic=regional_indic, post=post,
                               dis_indic=dis_indic, user_posts=user_posts, advisor_indic=advisor_indic)