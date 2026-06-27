from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), Length(min=4, max=32), Regexp(r"^\w+$", message="仅允许字母、数字、下划线")
    ])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=254)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=64)])
    confirm = PasswordField("Confirm", validators=[DataRequired(), EqualTo("password", message="两次密码不一致")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
