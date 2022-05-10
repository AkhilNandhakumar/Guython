{% include navigation.html %}

# Tech Talks - Trimester 3

<table>
    <tr>
        <td><a href="tt0">Tech Talk 0</a></td>
        <td><a href="tt1">Tech Talk 1</a></td>
        <td><a href="tt2">Tech Talk 2</a></td>
        <td><a href="tt3">Tech Talk 3</a></td>
    </tr>
</table>
<hr>

# Tech Talk 3 - Accounts and Login

## Flask_Login [Click here for Flask_Login Documentation](https://flask-login.readthedocs.io/en/latest/)
### Flask_Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your("Remember Me")  users’ sessions over extended periods of time. 

----

## MVC - Python/Flask Accounts and Login
[https://csp.nighthawkcodingsociety.com/crud/](https://csp.nighthawkcodingsociety.com/crud/)

### MVC - Initial Setup
[__init__.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/__init__.py) 
```python
# __init__.py  
from flask import Flask  

# Setup of key Flask object (app)
app = Flask(__name__)

from flask_login import LoginManager

# The most important part of an application that uses Flask-Login is the LoginManager class.
# You should create one for your application like this:  
# Setup LoginManager object (app)
login_manager = LoginManager()

# The login manager contains the code that lets your application and Flask-Login work together, 
# such as how to load a user from an ID,  where to send users when they need to log in, and the like.  
# Once the actual application object has been created, you can configure it for login with:

login_manager.init_app(app)

```

----

### MVC - MODEL

[model.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/model.py)
```python

# model.py
# The class that you use to represent users needs to implement these properties and methods:  
# is_authenticated, is_active, is_anonymous, get_id()
# To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations  
# for all of these properties and methods.

from flask_login import UserMixin
# Users DB is a collection Data Structure
class Users(UserMixin, db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.set_password(password) #encrypt password
        self.phone = phone

# required for login_user, overrides id (login_user default) to implemented userID
# The method get_id() must return a str that uniquely identifies this user, and can be used to load the user  
# from the user_loader callback.
def get_id(self):
    return self.userID

```
## Hashing Passwords With Werkzeug(German word meaning Tools)

Any time you want to login to a website/app, you need a password. It's very important not to store passwords as-is in a database, instead you need to do something called hashing which converts the password into a hash which is a big long string of text and characters.

Hashing is the process of scrambling raw information to the extent that it cannot reproduce it back to its original form. It takes a piece of information and passes it through a function that performs mathematical operations on the plaintext. This function is called the hash function, and the output is called the hash value/digest. Hashing is nearly impossible to revert, so if hackers get a hold of a database with hashed passwords, hash decoding is a futile task.  

<img width="520" alt="image" src="https://user-images.githubusercontent.com/88572244/161413976-32b5db62-56f4-4453-99c6-658bfbb995d1.png">

The Secure Hash Algorithm(SHA) with a digest size of 256 bits, or the SHA 256 algorithm, is one of the most widely used hash algorithms. While there are other variants, SHA 256 has been at the forefront of real-world applications.

**Werkzeug is a comprehensive WSGI web application library. It is a WSGI toolkit that implements requests, response objects, and utility functions. This enables a web frame to be built on it. The Flask framework uses Werkzeug as one of its bases.**

werkzeug.security methods generate_password_hash to create a hashed/encrypted password and, check_password_hash to check the hashed password

[model.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/model.py#L74-L83)
```python

from werkzeug.security import generate_password_hash, check_password_hash

 # set password method is used to create encrypted password
    def set_password(self, password):
        """Create hashed password."""
        * Procedural Abstraction
        self.password = generate_password_hash(password, method='sha256')

    # check password to check versus encrypted password
    def is_password_match(self, password):
        """Check hashed password."""
        result = check_password_hash(self.password, password)
        return result
```

----

### MVC - VIEW

[authorize.html](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/templates/cruddy/authorize.html), 
[login.html](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/templates/cruddy/login.html)

<img width="389" alt="image" src="https://user-images.githubusercontent.com/88572244/161989620-b023fa04-79dd-41ae-8320-6eb772730321.png">

```python
# authorize.html

# The conventional HTML Sign-up screen 

<div class="container bg-secondary py-4">
            <div class="p-5 mb-4 bg-light text-dark rounded-3">
                <form method="POST" ID="authUser" action={{url_for('crud.crud_authorize')}} >
                    <table>
                        <tr><th><label for="user_name">Username</label></th></tr>
                        <tr><td><input type="text" id='user_name' name="user_name" size="20" required></td></tr>
                        <tr><th><label for="email">Email</label></th></tr>
                        <tr><td><input type="email" id="email" name="email" size="20" required></td></tr>
                        Hack #1 Add Phone Number to Sign-Up screen  
                        <tr><th><label for="password1">Password</label></th></tr>
                        <tr><td><input type="password" id='password1' name="password1" size="20" required></td></tr>
                        <tr><th><label for="password2">Password Confirmation</label></th></tr>
                        <tr><td><input type="password" id='password2' name="password2" size="20" required></td></tr>
                        <tr><th><input type="submit" value="Submit"></th></tr>
                        <tr><td><a href={{url_for('crud.crud_login')}}>Log In</a></td></tr>
                    </table>
                </form>
            </div>
```

----

### MVC - CONTROL, View Driver

#### [app_crud.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/app_crud.py#L22-L33) under Data on nighthawkcodingsociety.com will now need a login with @login_required 

```python

flask_login.login_required
# If you decorate a view(route) with this, it will ensure that the current user is logged in and authenticated before calling the actual view. 
# (If they are not, it calls the LoginManager.unauthorized callback.). 
# Use this example for Hack #3.
@app_crud.route('/')
@login_required  # Flask-Login uses this decorator to restrict access to logged in users
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())

# Unauthorised users do not get access to the SQL CRUD
# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('crud.crud_login'))

```

----

### MVC - CONTROL, Model Driver

[query.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/cruddy/query.py)
```python

# query.py

from __init__ import login_manager, db
from cruddy.model import Users
from flask_login import current_user, login_user, logout_user

# login user based off of email and password
def login(email, password):
    # sequence of checks
    if current_user.is_authenticated:  # return true if user is currently logged in
        return True
    elif is_user(email, password):  # return true if email and password match
        user_row = user_by_email(email)
        login_user(user_row)  # sets flask login_user
        return True
    else:  # default condition is any failure
        return False


# this function is needed for Flask-Login to work.
# User_loader callback. This callback is used to reload the user object from the user ID stored in the session.   
# It should take the str ID of a user, and return the corresponding user object.  
# It should return None (not raise an exception) if the ID is not valid. 

@login_manager.user_loader
def user_loader(user_id):
    """Check if user login status on each page protected by @login_required."""
    if user_id is not None:
        return Users.query.get(user_id)
    return None


# Authorize new user requires user_name, email, password
def authorize(name, email, password):
    if is_user(email, password):
        return False   #email already exist in DB
    else:
        # auth_user is an object of class Users
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone="1234567890"  # this should be added to authorize.html Hack #1
        )
        # Password is encrypted in the init method of the class with self.set_password(password)
        # Add it to the auth_user object
        auth_user.create()
        return True


# logout user
Hack #2 Add logout to CRUD screen  
def logout():
    logout_user()  # removes login state of user from session
```
In a nutshell, how can we add authentication to our Flask app:  
* Initialize with  
   * Use the Flask-Login library for session management  
   * Use the built-in Flask utility for hashing passwords  
* Create Model  
  * Use Flask-SQLAlchemy to create a User model. Add password encryption with werkzeug.security  
* Create Views    
  * Create sign-up and login forms for the users to create accounts and log in
  * Add protected pages to the app for logged in users only
* Control(check against DB):
  * Flash error messages back to users when something goes wrong (email exists when on sign-up page or incorrect email/pwd when on login page)
  * Use information from the user’s account to display on the profile page
* Logout user

### TT3 Challenges/Hacks:  
Hack #1 Add Phone Number to Sign Up screen  
Hack #2 Add logout to CRUD screen. Display logged in User on top of CRUD Page  
Hack #3 Add login_required to another portion of project  

Additional features that you can add to your sponsor project.
* Add a "Remember Me" to the login page
* Validate email/password on login page
* Validate email, check for duplicate email on sign up page
* Add Login/Logout to navbar(grey or phase one out)
* Add lock symbol to menu items when running as anonymous

