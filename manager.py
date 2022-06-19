# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 13:50
# @Author   : Runke Zhong
# @Software : PyCharm


from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from application import app, db
from common.libs.exts import create_db
import www

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)
# manager.add_command("create_db", create_db)
manager.add_command("runserver", Server(host='127.0.0.1', port=8000, use_debugger=True))



def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback

