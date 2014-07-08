from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.orm import sessionmaker



engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
										autocommit = False,
										autoflush= False)) 

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key =True)
	first_name = Column(String(64), nullable=True)
	last_name= Column(String(64), nullable=True)
	telephone= Column(String(64), nullable=True)
	address= Column(String(64), nullable=True)
	ICE= Column(String(64), nullable=True)
	email = Column(String(64), nullable=True)
	password = Column(String(64), nullable=True)

class Appointment(Base):
	__tablename__ = "appointments"

	"""not completely sure what information I need to collect here."""

class Dog(Base):
	__tablename__ = "dogs"
	__table_args__ = {'sqlite_autoincrement': True}

	id = Column(Integer, primary_key=True)
	vet_id = Column(Integer, ForeignKey('vets.id'))
	name = Column(Integer, nullable=True)
	breed = Column(Integer, nullable=True)
	age = Column(String(64), nullable=True)
	gender = Column(String(64), nullable=True)
	weight = Column(String(64), nullable=True)

class Dog_Appointment(Base):
	__tablename__ = "dog_appointemts"
	__table_args__ = {'sqlite_autoincrement': True}

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	appointment_id = Column(Integer, ForeignKey('appointments.id'))

class User_Dog(Base):
	__tablename__ = "user_dogs"
	__table_args__ = {'sqlite_autoincrement': True}

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	dog_id = Column(Integer, ForeignKey('dogs.id'))

class Veterinarian(Base):
	__tablename__ = "veterinarians"

	id = Column(Integer, primary_key=True)
	first_name = Column(Integer, nullable=True)
	last_name = Column(Integer, nullable=True)
	address = Column(Integer, nullable=True)
	telephone = Column(Integer, nullable=True)

class Payment(Base):
	__tablename__ = "payments"

	id = Column(Integer, primary_key=True)


	

	""" KEEPING THIS BECAUSE I DON'T KNOW WHAT IT IS AND IT MAYBE IMPORTANT
	user = relationship("User", 
		backref=backref("ratings", order_by=id))"""
	


### End class declarations

def main():
	"""In case we need this for something"""
	pass

if __name__ == "__main__":
	main()
