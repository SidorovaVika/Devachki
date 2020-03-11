from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp,ValidationError
from models.user import User


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])

    def validate_email(self, email):
        if User.query.filter(User.email==email.data).first() is None:
            raise ValidationError("Неверно введен E-mail")