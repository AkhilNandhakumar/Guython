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
def authorize(name, email, password, phone):
    if is_user(email, password):
        return False   #email already exist in DB
    else:
        # auth_user is an object of class Users
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone=phone  # this should be added to authorize.html Hack #1
        )
        # Password is encrypted in the init method of the class with self.set_password(password)
        # Add it to the auth_user object
        auth_user.create()
        return True


# logout user
# Hack 2 Add logout to CRUD screen
def logout():
    logout_user()
# removes login state of user from session
