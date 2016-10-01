from flask.views import MethodView
from flask import Flask, render_template, session, flash, request, session
from models.users import User, db_sesssion


class signup(MethodView):

	def get(self):
		return render_template('signup.html')

	def post(slef):
		form_username = request.form['username']
		form_password = request.form['password']
		alreay_created = db_sesssion.query(User).filter(User.username == form_username).first()
		if(form_username):
			flash("some already used this username")
			return redirect('/signup')
		else:
			new_user = User(form_username, form_password);
			try:
				db_sesssion.add(new_user)
				db_sesssion.commit()
				session['logged_in'] = True
				session['username'] = form_username
			except Exception as e:
				db_sesssion.rollback()
				db_sesssion.flush()
			return redirect('/')


class login(MethodView)

		def get(self):
			return render_template('login.html')
			
		def post(self):
			form_username = request.form['username']
			form_password = request.form['password']
			user = db_sesssion.query(User).filter(User.username == form_username, User.password == form_password).first()
			if(user):
				session['logged_in'] = True
				session['username'] = user.username
				return redirect('/profile')
			else:
				flash("your username or password was enterned incorect")
				return redirect('/login')


class profile(MethodView):

	def get(self, username)
		user = db_sesssion.query(User).filter(User.username = username).first()
		query = {
			username: user.username,
			link1: user.link_one,
			link2: user.link_two,
			link3: user.link_three,
			link4: user.link_four,
			link5: user.link_five
		}
		return render_template('profile')

	def post(self):
				





