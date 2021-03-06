from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from project.models.user import User



class SignupForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    phone = StringField('Телефон', validators=[DataRequired(), Regexp('^((\+7|7|8)+([0-9]){10})$',
                                                                      message='Некорректный формат телефона')])
    department = SelectField("Отделение",
                             choices=[('Юго-Западное', 'Юго-Западное'), ('Северо-Восточное', 'Северо-Восточное'),
                                      ('Центральное', 'Центральное'), ('Северное', 'Северное'), ('Южное', 'Южное'),
                                      ('Восточное', 'Восточное'), ('Западное', 'Западное'),
                                      ('Юго-Восточное', 'Юго-Восточное'), ('Северо-Западное', 'Северо-Западное'),
                                      ('Красногвардейское', 'Красногвардейское'), ('Московское', 'Московское'),
                                      ('Василеостровское', 'Василеостровское'), ('Невское', 'Невское'),
                                      ('Адмиралтейское', 'Адмиралтейское'), ('Приморское', 'Приморское'),
                                      ('Кировское', 'Кировское'), ('Калиниское', 'Калиниское'),
                                      ('Курортное', 'Курортное'), ('Фрунзенское', 'Фрунзенское'),
                                      ('Пушкинское', 'Пушкинское'), ('Петроградское', 'Петроградское'),
                                      ('Выборгское', 'Выборгское'), ('Волоколамское', 'Волоколамское'),
                                      ('Егорьевское', 'Егорьевское'), ('Клинское', 'Клинское'),
                                      ('Раменское', 'Раменское'), ('Тверское', 'Тверское'),
                                      ('Правобережное', 'Правобережное'), ('Левобережное', 'Левобережное'),
                                      ('Северное', 'Северное'), ('Южное', 'Южное'), ('Дзержинское', 'Дзержинское'),
                                      ('Заельцовское', 'Заельцовское'), ('Центральное', 'Центральное'),
                                      ('Первомайское', 'Первомайское')])

    password = PasswordField('Пароль', validators=[DataRequired()])

    def validate_email(self, email):
        if User.query.filter(User.email == email.data).first():
            raise ValidationError("Данный E-mail уже зарегистрирован")
