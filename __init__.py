from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

# Setup custom application variables
app.config['UPLOAD_FOLDER'] = 'static/uploads/'     # user uploaded content
app.config['NEXT_PAGE'] = None                      # next page on login attempt
