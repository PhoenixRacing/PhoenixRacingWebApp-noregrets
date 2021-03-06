from flask import render_template, request, redirect, flash, url_for
from flask.ext.login import login_user
from ..models import LogInForm
from ..models import User
from ..models import Notify

def login():

	def invalidCredentials():
		notification = Notify(notification_type = 'error', message = 'Invalid Username or Password')
		return  render_template('login.html', form=form, active_page='login', notify = notification)

	form = LogInForm(request.form)
	if request.method == 'POST' and form.validate():

		# Check existence of user
		user = User.objects(email = form.data['email'])
		if user.count() < 1:
			return invalidCredentials()
		
		user = user.first()
		
		# Check correctness of password
		if user.check_password(form.data['password']):
			login_user(user)
			return redirect(url_for('index'))
		else:
			return invalidCredentials()
	return render_template('login.html', form=form, active_page='login')