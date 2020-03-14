from app import create_app
import click
import csv
from models.departments import Department
from models import db
from models.user import User
from models.user_department import UserDepartment

app = create_app()

@app.cli.command('create-department')
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

@app.cli.command('clear_bd')
def clear_bd():
    db.session.remove()
    db.drop_all()
    db.session.commit()

@app.cli.command('create-users')
def create_users():
    for i in range(19):
        with open("users/users_{}.csv".format(i), newline='') as csvfile:
            r = csv.reader(csvfile, delimiter=';')
            for row in r:
                db.session.add(User(name=row[1], surname=row[0],email=row[2],phone=row[3],password="1234"))
                db.session.add(UserDepartment(user_id=)
        #db.session.commit()


if __name__ == '__main__':
    app.cli()