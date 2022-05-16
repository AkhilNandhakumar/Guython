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
    name = db.Column(db.String(255), unique=True, nullable=True)
    event = db.Column(db.String(255), unique=False, nullable=False, primary_key=True)
    day = db.Column(db.Integer, unique=False, nullable=False)
    month = db.Column(db.Integer, unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, event, day, month, year):
        self.name = name
        self.event = event
        self.day = day
        self.month = month
        self.year = year

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
            "name": self.name,
            "event": self.event,
            "day": self.day,
            "month": self.month,
            "year": self.year,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, event, day, month, year):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(event) > 0:
            self.event = event
        if int(day) > 0:
            self.day = day
        if int(month) > 0:
            self.month = month
        if int(year) > 2021:
            self.year = year
        else:
            self.year = 2022
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None