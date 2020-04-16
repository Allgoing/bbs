# -- coding: utf-8 --

from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import Email, InputRequired, Length, EqualTo
from ..base_forms import BaseForm
from utils import cache
from flask import g


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱地址'), InputRequired(message='请输入邮箱地址')])
    password = StringField(validators=[Length(6, 20, message='请输入长度在6到20位的密码')])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message='请输入长度在6到20位的密码')])
    newpwd = StringField(validators=[Length(6, 20, message='请输入长度在6到20位的密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd", message='请保持新旧密码一致')])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    captcha = StringField(validators=[Length(6, 6, message='验证码长度为6位')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        cache_captcha = cache.get(email)
        if not cache_captcha or captcha.lower() != cache_captcha.lower():
            raise ValidationError('邮箱验证码错误!')

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱！')



