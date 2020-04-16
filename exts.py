# -- coding: utf-8 --

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils.sms_sender import SmsSender

db = SQLAlchemy()
mail = Mail()
sms_sender = SmsSender()