from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()
engine = create_engine('sqlite:///data.db', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()


class User(Base):
	id = Column('user_id', Integer, primary_key=True)
	username = Column(String(50))
	password = Column(String(50))
	link_one = Column(String(500))
	link_two = Column(String(500))
	link_three = Column(String(500))
	link_four = Column(String(500))
	link_five = Column(String(500))
	link_one_title = Column(String(100))
	link_two_title = Column(String(100))
	link_three_title = Column(String(100))
	link_four_title = Column(String(100))
	link_five_title = Column(String(100))
	__tablename__ = "User"

	def __init__(self, username, password, link_one, link_two, link_three, link_four, link_five
				,link_one_title, link_two_title, link_three_title, link_four_title, link_five_title):
		self.username = username
		self.password = set_password(password)
		self.link_one = link_one
		self.link_two = link_two
		self.link_three = link_three
		self.link_four = link_four
		self.link_five = link_five
		self.link_one_title =  link_one_title
		self.link_two_title = link_two_title
		self.link_three_title = link_three_title
		self.link_four_title = link_four_title
		self.link_five_title = link_five_title

	def set_password(self, password):
		self.pw_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)


Base.metadata.create_all(engine)




