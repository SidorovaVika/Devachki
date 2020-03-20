from app import create_app
import click
import csv
from models.departments import Department
from models import db
from models.user import User
from models.advisory_board import Advisor
from models.user_department import UserDepartment
from werkzeug.security import generate_password_hash
import datetime
import random

app = create_app()

@app.cli.command('create-departments')
@click.argument('csvfile', nargs=1)
def create(csvfile):
    db.session.add(Department(name="Федеральное отделение", parent_id=None, level=1))
    with open(csvfile, newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=';')
        for row in r:
            if row[0]!="Региональное отделение":
                if not(Department.query.filter(Department.name==row[0]).first()):
                    db.session.add(Department(name=row[0], parent_id=1, level=2))
                db.session.add(Department(name=row[2], parent_id=Department.query.filter(Department.name==row[0]).first().id, level=3))
    db.session.commit()

@app.cli.command('clear-bd')
def clear_bd():
    db.session.remove()
    db.drop_all()
    db.session.commit()
    db.create_all()

@app.cli.command('create-users')
@click.argument('csvfile', nargs=1)
@click.argument('dep_id', nargs=1)
def create_users(csvfile,dep_id):
    if not(User.query.filter(User.email=="important@mail.ru").first()):
        user = User(name="Главный", surname="Самый", email="important@mail.ru", phone="+79215729636",
                    password=generate_password_hash("1234"))
        db.session.add(user)
        db.session.commit()
        user_dep_id = UserDepartment(user_id=user.id, department_id=Department.query.filter(
            Department.name == "Московское").first().id, post="Руководитель Федерального Отделения",
                                     employment_date=datetime.date.today(), dismissal_date=None)
        db.session.add(user_dep_id)
        db.session.commit()
    with open(csvfile, newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=';')
        for row in r:
            db.session.add(User(name=row[1], surname=row[0],email=row[2],phone=row[3],password=generate_password_hash("1234")))
            db.session.commit()
            if row[4]=="":
                row[4]=None
            if row[5]=="":
                row[5]=None
            if len(row)>6:
                if row[6]=="":
                    row[6]=None
                if row[7]=="":
                    row[7]=None
            db.session.add(UserDepartment(user_id=User.query.filter(User.email==row[2]).first().id,department_id=int(dep_id),post="Пользователь",employment_date=row[4],dismissal_date=row[5]))
            db.session.commit()

@app.cli.command('create-random-users')
def create_random_users():
    if not(User.query.filter(User.email=="important@mail.ru").first()):
        user = User(name="Главный", surname="Самый", email="important@mail.ru", phone="+79215729636",
                    password=generate_password_hash("1234"))
        db.session.add(user)
        db.session.commit()
        user_dep_id = UserDepartment(user_id=user.id, department_id=Department.query.filter(
            Department.name == "Московское").first().id, post="Руководитель Федерального Отделения",
                                     employment_date=datetime.date.today(), dismissal_date=None)
        db.session.add(user_dep_id)
        db.session.commit()
    for i in range(20):
        print(i)
        with open('users/users_{}.csv'.format(i), newline='') as csvfile:
            r = csv.reader(csvfile, delimiter=';')
            for row in r:
                if not(User.query.filter(User.email==row[2]).first()):
                    db.session.add(User(name=row[1], surname=row[0],email=row[2],phone=row[3],password=generate_password_hash("1234")))
                    db.session.commit()
                    loc_deps_id = [i.id for i in Department.query.filter(Department.level == 3).all()]
                    dep_id=random.choice(loc_deps_id)
                    if row[4]=="":
                        row[4]=None
                    if row[5]=="":
                        row[5]=None
                    if len(row)>6:
                        if row[6]=="":
                            row[6]=None
                        if row[7]=="":
                            row[7]=None
                        db.session.add(Advisor(user_id=User.query.filter(User.email == row[2]).first().id,
                                               department_id=dep_id,
                                               employment_date=row[6], dismissal_rate=row[7]))
                        db.session.commit()
                        db.session.add(UserDepartment(user_id=User.query.filter(User.email == row[2]).first().id,
                                                      department_id=dep_id, post="Сотрудник",
                                                      employment_date=row[4], dismissal_date=row[5]))
                        db.session.commit()
                    else:
                        db.session.add(UserDepartment(user_id=User.query.filter(User.email==row[2]).first().id,department_id=random.choice(loc_deps_id),post="Пользователь",employment_date=row[4],dismissal_date=row[5]))
                        db.session.commit()
                    print('Успех')

if __name__ == '__main__':
    app.cli()