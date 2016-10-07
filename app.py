from flask import Flask, render_template
from views.main import home, search
from views.userViews import signup, login, profile, logout
from urls.main import main

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "#*&IYREYF*&SDYFI"
app.register_blueprint(main)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.add_url_rule('/', view_func= home.as_view('home'))
app.add_url_rule('/search', view_func= search.as_view('search'))
app.add_url_rule('/login', view_func=login.as_view('signup'))
app.add_url_rule('/signup', view_func=signup.as_view('login'))
app.add_url_rule('/profile/<username>', view_func=profile.as_view('profile'))
app.add_url_rule('/logout', view_func=logout.as_view('logout'))

if(__name__ == "__main__"):
	app.run()