from app import create_app, db
from app.models import User, Comment, Blog, Role
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# app = create_app('test')
app = create_app('development')
# app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Comment = Comment, Blog = Blog, Role = Role)

if __name__=='__main__':
  manager.run()