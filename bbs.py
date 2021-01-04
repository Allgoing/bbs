from flask import Flask
from app.cms import cms_bp
from app.common import common_bp
from app.front import front_bp
from app.ueditor import bp
import config
from exts import db, mail, sms_sender
from flask_wtf import CSRFProtect


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(bp)

    db.init_app(app)
    mail.init_app(app)
    # sms_sender.init_app(app)
    CSRFProtect(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
