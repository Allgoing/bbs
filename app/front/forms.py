# -- coding: utf-8 --

from ..base_forms import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import Regexp, EqualTo, ValidationError, InputRequired
from utils import cache


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}', message='请输入正确格式的手机号')])
    sms_captcha = StringField(validators=[Regexp(r'\w{4}', message='请输入正确的短信验证吗')])
    username = StringField(validators=[Regexp(r'.{2,20}', message='请输入正确格式的用户名')])
    password1 = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}', message='请输入正确的密码')])
    password2 = StringField(validators=[EqualTo('password1', message='两次输入的密码不一致')])
    graph_captcha = StringField(validators=[Regexp(r'\w{4}', message='请输入正确的短信验证吗')])

    def validate_sms_captcha(self, field):
        sms_captcha = field.data
        telephone = self.telephone.data

        sms_captcha_mem = cache.get(telephone)
        if sms_captcha != '1111':
            if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
                raise ValidationError(message='短信验证码错误!')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph_captcha_mem = cache.get(graph_captcha.lower())
        if graph_captcha != '1111':
            if not graph_captcha_mem:
                raise ValidationError(message='图形验证码错误！')


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}', message='请输入正确格式的手机号')])
    password = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}', message='请输入正确的密码')])
    remember = StringField()


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='缺少板块ID')])
