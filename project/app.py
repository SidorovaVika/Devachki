from flask import Flask
from models import db
from views import MainView, LoginView, LogoutView, SignupView
from flask import render_template
from flask_login import LoginManager
from components.auth import load_user

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lecture:q556A8kLUrQU@/sidorova?host=rc1b-80ql678cqoo4jq71.mdb.yandexcloud.net&port=6432'
    app.config.update(SECRET_KEY='secret_xxx')
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.user_loader(load_user)
    app.add_url_rule('/',view_func=MainView.as_view('main'),methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
    app.add_url_rule('/login', view_func=LoginView.as_view('login'),methods=['GET', 'POST'])
    app.add_url_rule('/signup', view_func=SignupView.as_view('signup'),methods=['GET', 'POST'])
    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from models import *
        db.create_all()
    app.run()