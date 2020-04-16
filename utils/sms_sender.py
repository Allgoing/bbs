# -- coding: utf-8 --
# -- coding: utf-8 --

import requests
import json
import logging
from utils.captcha import Captcha


class SmsSender(object):

    APP_KEY_FIELD = 'FEIGEI_APP_KEY'
    APP_SECRET_FIELD = 'FEIGEI_APP_SECRET'
    APP_TEMPLATE_CODE = 'FEIGEI_TEMPLATE_CODE'

    def __init__(self, app=None):
        self.url = 'https://u.ifeige.cn/api/message/send'
        self.header = {'content-type': 'application/json'}
        self.key = '70865c22185afbcd326dbcb2b9fabc4d'
        self.secret = '12df0c04fec72d0aae0014ec01b5d276'
        self.template = 'UZvQwUiQeY-scmoMsi-IOeR_DNW6ZLs6xhnUUTWfjNw'
        self.sms_captcha = None
        self.telephone = None

    #     if app:
    #         self.init_app(app)
    #
    # def init_app(self, app):
    #     config = app.config
    #     try:
    #         self.key = config[self.APP_KEY_FIELD]
    #         self.secret = config[self.APP_SECRET_FIELD]
    #         self.template = config[self.APP_TEMPLATE_CODE]
    #     except Exception as e:
    #         logging.error(e.args)
    #         raise ValueError('请填写正确的飞鸽快信的配置')

    def send_sms(self, telephone, captcha):
        # self.sms_captcha = Captcha.gene_text(number=number)
        self.telephone = telephone
        data = {
            'secret': self.secret,
            'app_key': self.key,
            'template_id': self.template,
            'url': '',
            'data': {
                'first': {
                    'value': self.telephone,
                    'color': '#173177'
                },
                'order': {
                    'value': captcha,
                    'color': '#173177'
                },
                'remark': {
                    'value': '验证成功',
                    'color': '#173177'
                }
            }
        }
        response = requests.post(url=self.url, headers=self.header, data=json.dumps(data))
        result = response.json()
        if result['code'] == 200:
            return True
        else:
            print(result)
            return False
