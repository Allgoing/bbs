# -- coding: utf-8 --
from flask import g, session

from .cms_views import cms_bp
import config
from .models import CMSUser, CMSPermission


@cms_bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user


@cms_bp.context_processor
def cms_context_processor():
    return {'CMSPermission': CMSPermission}
