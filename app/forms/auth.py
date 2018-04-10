# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User

__author__ = 'Alimazing'

class LoginForm(Form):
	email = StringField(validators=[
		DataRequired(), Length(8, 64), Email(message='电子邮件不符合规范')])

	password = PasswordField(validators=[
		DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

class RegisterForm(LoginForm):
	nickname = StringField(validators=[
		DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('电子邮件已被注册')

	def validate_nickname(self, field):
		if User.query.filter_by(nickname=field.data).first():
			raise ValidationError('昵称已存在')
