from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Tên người dùng này đã được sử dụng! Hãy thử tên người dùng khác')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Địa chỉ Email này đã được sử dụng! Hãy thử địa chỉ Email khác')

    username = StringField(label='Tên người dùng:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Mật khẩu:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Nhập lại mật khẩu:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Tạo tài khoản')

class LoginForm(FlaskForm):
    username = StringField(label='Tên người dùng:', validators=[DataRequired()])
    password = PasswordField(label='Mật khẩu:', validators=[DataRequired()])
    submit = SubmitField(label='Đăng nhập')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')