# In order to use Flask-Migrate we imported Manager as well as Migrate 
# and MigrateCommand to our manage.py file. We also imported app and db
# so we have access to them from within the script.

# First, we set our config to get our environment,  based on the
# environment variable, created a migrate instance, with app and db
# as the arguments, and set up a manager command to initialize a
# Manager instance for our app. Finally, we added the db command
# to the manager so that we can run the migrations from the command
# line.

import os
from flask_script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()