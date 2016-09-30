from flask.views import View
from flask import Flask
from flask import render_template, redirect

class home(View):

	def dispatch_request(self):
		return render_template("home.html")




