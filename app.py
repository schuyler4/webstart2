from flask import Flask
from views.main import home
from urls.main import main

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "#*&IYREYF*&SDYFI"
app.register_blueprint(main)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.add_url_rule('/', view_func= home.as_view('home'))



if(__name__ == "__main__"):
	app.run()