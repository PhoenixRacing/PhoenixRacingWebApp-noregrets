from flask import render_template
from flask.ext.login import current_user

def donate():
	return render_template('donate_temp.html', active_page='donate')