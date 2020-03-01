from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from models.user import User
from models.departments import Department




class SignupForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    phone = StringField('Телефон', validators=[DataRequired(),Regexp('^((\+7|7|8)+([0-9]){10})$',message='Некорректный формат телефона')])
    department=SelectField("Отделение", choices=[('Архангельск', 'Архангельск'), ('Котлас', 'Котлас'), ('Северодвинск', 'Северодвинск'), ('Тихвин', 'Тихвин'), ('Тосно', 'Тосно'), ('Луга', 'Луга'), ('Печоры', 'Печоры'), ('Невель', 'Невель'), ('Пустошка', 'Пустошка')])

    password = PasswordField('Пароль', validators=[DataRequired()])
    def validate_email(self, email):
        if User.query.filter(User.email==email.data).first():
            raise ValidationError("Данный E-mail уже зарегистрирован")