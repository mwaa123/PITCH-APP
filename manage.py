from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Comments,Add,UpVote,DownVote

# Creating app instance
app = create_app('development')
# app = create_app('production')
manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def shell():
    return dict(app = app,db = db,User = User, Add = Add, Comments = Comments)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    db.init_app(app)
    manager.run()

