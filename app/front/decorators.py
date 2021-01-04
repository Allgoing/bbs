# -- coding: utf-8 --
from flask import session, redirect, url_for
from functools import wraps
import config


# 登录
def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.signin'))
    return inner