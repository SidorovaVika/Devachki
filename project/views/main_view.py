from flask.views import View
from flask import render_template, request
from flask_login import current_user

class MainView(View):
    def dispatch_request(self):

        return render_template('main.html', indic=current_user.is_authenticated)