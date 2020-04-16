# -- coding: utf-8 --
import os

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'bbs'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER,
                                                                       USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'abcdef'
FRONT_USER_ID = 'dfnadfamdfnadfnadfasmdfdsaf'

# 发送者邮箱服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT : "587"
MAIL_USE_TLS = True
# MAIL_USE_SSL : default False
MAIL_USERNAME = '3162909642@qq.com'
MAIL_PASSWORD = 'hdvnaxyzhdcmddca'
MAIL_DEFAULT_SENDER = '3162909642@qq.com'

# 飞鸽快信配置
FEIGEI_APP_KEY = '70865c22185afbcd326dbcb2b9fabc4d'
FEIGEI_APP_SECRET = '12df0c04fec72d0aae0014ec01b5d276'
FEIGEI_TEMPLATE_CODE = 'UZvQwUiQeY-scmoMsi-IOeR_DNW6ZLs6xhnUUTWfjNw'
