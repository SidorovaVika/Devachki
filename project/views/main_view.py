from flask.views import View
from flask import render_template, redirect, url_for
from flask_login import current_user


class MainView(View):
    def dispatch_request(self):
        if current_user.is_authenticated:
            return redirect(url_for('user', user_id=current_user.get_id()))
        return render_template('main.html')