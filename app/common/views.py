# -- coding: utf-8 --

from flask import Blueprint, request, make_response
from utils import restful, cache
from exts import sms_sender
from .forms import SMSCaptchaForm
from utils.captcha import Captcha
from io import BytesIO


common_bp = Blueprint('common', __name__, url_prefix='/c')


@common_bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)

        if sms_sender.send_sms(telephone, captcha):
            cache.set(telephone, captcha)
            return restful.success()
        else:
            return restful.params_error()
    else:
        return restful.params_error(message='参数错误')


@common_bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    cache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp
