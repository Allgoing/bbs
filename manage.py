# -- coding: utf-8 --

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from bbs import create_app
from exts import db
from app.cms import models as cms_models
from app.front import models as front_models
from app.models import BannerModel, BoardModel, PostModel

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPermission
FrontUser = front_models.FrontUser

app = create_app()

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')


@manager.command
def create_role():
    # 访问者
    visitor = CMSRole(name='访问者', desc='只能访问相关数据，不能修改')
    visitor.permissions = CMSPermission.VISITOR

    # 运营角色(修改个人信息，管理帖子，管理评论，管理前台用户)
    operator = CMSRole(name='运营', desc='管理帖子，管理评论，管理前台用户')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER

    # 管理员
    admin = CMSRole(name='管理员', desc='拥有所有权限')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.FRONTUSER | CMSPermission.COMMENTER | CMSPermission.POSTER \
                        | CMSPermission.BOARDER | CMSPermission.CMSUSER

    # 开发
    developer = CMSRole(name='开发者', desc='开发专用')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加角色成功')
        else:
            print('不存在%s这个权限' % name)
    else:
        print('%s不存在这个邮箱用户' % email)


@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)
    db.session.commit()


@manager.command
def test_permission():
    user = CMSUser.query[1]
    if user.has_permission(CMSPermission.VISITOR):
        print('访问者')
    else:
        print('不是访问者')


if __name__ == '__main__':
    manager.run()
