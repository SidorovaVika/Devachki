from flask.views import View
from flask import redirect, url_for

class LocalView(View):
    def dispatch_request(self):
        return redirect(url_for('local'))