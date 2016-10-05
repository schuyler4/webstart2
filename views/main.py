from flask.views import View, MethodView
from flask import *
from flask import render_template, redirect
from models.users import db_session, User

class home(MethodView):
	
	def get(self):
		username = session.get('username')
		user = db_session.query(User).filter(User.username == username)
		return render_template('home.html')

	def post(self):
		search = request.form['search']
		return redirect('/')

