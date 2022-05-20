""" database dependencies to support Users db examples """
from __init__ import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along

# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Calendar(UserMixin, db.Model):
    # define the Users schema
    eventID = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    event = db.Column(db.String(255), unique=True, nullable=False)
    day = db.Column(db.Integer, unique=False, nullable=False)
    yearmonth = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, event, day, yearmonth):
        self.name = name
        self.event = event
        self.day = day
        self.yearmonth = yearmonth

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "eventID": self.eventID,
            "name": self.name,
            "event": self.event,
            "day": self.day,
            "yearmonth": self.yearmonth,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, event, day, yearmonth):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(event) > 0:
            self.event = event
        if 32 > int(day) > 0:
            self.day = day
        else:
            self.day = 1
        if len(yearmonth) > 0:
            self.yearmonth = yearmonth
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along

# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
#
# # Define the Users table within the model
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) Users represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL








