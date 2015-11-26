# -*- coding:utf-8 -*-

import os
from flask_script import Manager
from TgwlDataCenter import create_app, db
from TgwlDataCenter.models import Fruit

app = create_app(os.getenv('TGWL_CONFIG') or 'default')
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Fruit=Fruit)

if __name__ == '__main__':
    manager.run()
