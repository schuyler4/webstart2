from flask import Flask
from views.main import home
from views.users import signup, login, profile
from urls.main import main

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "#*&IYREYF*&SDYFI"
app.register_blueprint(main)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.add_url_rule('/', view_func= home.as_view('home'))
app.add_url_rule('/login', view_func=signup.as_view('signup'))
app.add_url_rule('/signup', view_func=login.as_view('login'))
app.add_url_rule('/profile/<username>', view_func=profile.as_view('profile'))


if(__name__ == "__main__"):
	app.run()