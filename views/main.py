from flask.views import View, MethodView
from flask import *
from flask import render_template, redirect
from models.users import db_session, User

class home(MethodView):
	
	def get(self):
		username = session.get('username')
		user = db_session.query(User).filter(User.username == username)
		logged_in = False
		if session.get('logged_in'):
			logged_in = True

		return render_template('home.html', logged_in = logged_in, username = username)

	def post(self):

		all_users = db_session.query(User).all()
		search_query = request.form['searching']
		session['query_array_url'] = []
		session['query_array_title'] = []
		session.finds = session[]
		for user in all_users:
			query_array_url.append(user.link_one)
			query_array_url.append(user.link_two)
			query_array_url.append(user.link_three)
			query_array_url.append(user.link_four)
			query_array_url.append(user.link_five)

			query_array_title.append(user.link_one_title)
			query_array_title.append(user.link_two_title)
			query_array_title.append(user.link_three_title)
			query_array_title.append(user.link_four_title)
			query_array_title.append(user.link_five_title)

		return redirect('/search')
		

		





