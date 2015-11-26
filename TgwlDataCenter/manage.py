# -*- coding:utf-8 -*-

import os
from flask_script import Manager
from TgwlDataCenter import create_app

app = create_app(os.getenv('TGWL_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
