from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from models.user import User


class SignupForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    phone = StringField('Телефон', validators=[DataRequired(),Regexp('^((\+7|7|8)+([0-9]){10})$',
message='Некорректный формат телефона')])
    password = StringField('Пароль', validators=[DataRequired()])

    def validate_email(self, email):
        if User.query.filter(User.email==email.data).first():
            raise ValidationError("Данный E-mail уже зарегистрирован")