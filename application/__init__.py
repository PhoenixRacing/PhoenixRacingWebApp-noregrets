import flask
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager, current_user
from flask.ext.bcrypt import Bcrypt
from functools import wraps

# Setup the app object
app = Flask(__name__)

# Setup BCrypt
flask_bcrypt = Bcrypt(app)

# Setup the Database
app.config.from_pyfile('mongo_config.cfg')
db = MongoEngine(app)

# Setup the log in system
login_manager = LoginManager()
login_manager.init_app(app)

# Setup globals in the views
def render_decorator(f):
	@wraps(f)
	def dec(*args,**kwargs):
		# always add the current user to the view
		return f(*args,user=current_user,**kwargs)
	return dec

flask.render_template = render_decorator(flask.render_template)

# The router cannot run until the app and database are created
import router

if __name__ == "__main__":
	app.run()