from . import app
import controllers

@app.route("/")
@app.route("/index/")
def index():
	return controllers.index()

@app.route("/login/", methods=['GET', 'POST'])
def login():
	return controllers.login()

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	return controllers.signup()

@app.route("/data/", methods=['GET','POST'])
def data():
	return controllers.data()

@app.route("/subteams/")
def subteams():
	return controllers.subteams()

@app.route("/subteams/<subteam_name>/")
def subteam_description(subteam_name):
	return controllers.description(subteam_name)

@app.route("/donate/")
def donate():
	return controllers.donate()

@app.route("/sponsors/")
def sponsors():
	return controllers.sponsors()

@app.route("/chassis/")
def chassis():
	return controllers.description('chassis')

@app.route("/drivetrain/")
def drivetrain():
	return controllers.description('drivetrain')

@app.route("/suspension/")
def suspension():
	return controllers.description('suspension')

@app.route("/electrical/")
def electrical():
	return controllers.description('electrical')