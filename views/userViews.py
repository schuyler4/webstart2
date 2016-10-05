from flask.views import MethodView
from flask import Flask, render_template, session, flash, request, session, redirect
from models.users import User, db_session
from sqlalchemy import *
from sqlalchemy.orm import *


class signup(MethodView):

	def get(self):
		return render_template('signup.html')

	def post(self):
		form_username = request.form['username']
		form_password = request.form['password']
		alreay_created = db_session.query(User).filter(User.username == form_username).first()
		if(alreay_created):
			flash("some already used this username")
			return redirect('/signup')
		else:
			new_user = User(form_username, form_password, None, None, None, None, None, None, None, None, None, None);
			try:
				db_session.add(new_user)
				db_session.commit()
				session['logged_in'] = True
				session['username'] = form_username
			except Exception as e:
				db_session.rollback()
				db_session.flush()
			print("redirecting")
			return redirect('/profile/' + form_username)


class login(MethodView):

		def get(self):
			return render_template('login.html')
			
		def post(self):
			form_username = request.form['username']
			form_password = request.form['password']
			user = db_session.query(User).filter(User.username == form_username, User.password == form_password).first()
			if(user):
				session['logged_in'] = True
				session['username'] = user.username
				return redirect('/profile/' + user.username)
			else:
				flash("your username or password was enterned incorect")
				return redirect('/login')


class profile(MethodView):

	def get(self, username):
		logged_in = session['logged_in']
		user = db_session.query(User).filter(User.username == username).first()
		print(user.link_one)
		print(user.link_two)
		print(user.link_three)
		print(user.link_four)
		print(user.link_five)
		if(logged_in or session['username'] == user.username):
			username = user.username;
			return render_template('profile.html', 
			username = user.username,
			link_one = user.link_one,
			link_two = user.link_two,
			link_three = user.link_three,
			link_four = user.link_four,
			link_five = user.link_five,
			link_one_title = user.link_one_title,
			link_two_title = user.link_two_title,
			link_three_title = user.link_three_title,
			link_four_title = user.link_four_title,
			link_five_title = user.link_five_title)

		else:
			return redirect('/login')

	def post(self):
		user = db_session.query(Usre).filter(User.username == username).first()
		link_title = request.form['link_title']
		link_url = request.form['link_url']
		if(user.link_one == '' or user.link_two == '' or user.link_three == '' or user.link_four == '' or user.link_five == ''):

			all_links_url = [user.link_one, user.link_two, user.link_three, user.link_four, user.link_five]
			all_links_title = [user.link_one_title, user.link_two_title, user.link_three_title, user.link_four_title, user.link_five_title]

			for link_url in all_links_url:
				for link_title in all_links_title:
					if link_url == None and link_title == None:
						link_url = link_url
						link_title = link_title

			user.update({'link_one_title':'hello', 'link_one_url':'hello'})

			try:
				db_session.commit()
				print("suckess")
			except Exception as e:
				print("failure")
				db_session.rollback()
				db_session.flush()
	
		else:
			flash("all you links are used up")
		return redirect('profile/' + user.username)


class logout(MethodView):

	 def get(self):
	 	session['logged_in'] = False
	 	session['username'] = None
	 	return redirect('/')
			