from __init__ import app
from flask import Flask, request, Blueprint, render_template

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from student_calendar.app_calendar import app_calendar
from topics import app_topics
from learning import app_learning
from popcorncritics import app_popcorn

# GUYTHON APP REGISTERS
app.register_blueprint(app_learning)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_calendar)
app.register_blueprint(app_topics)
app.register_blueprint(app_popcorn)

@app.route('/')
def mainpage():
    return render_template("main_page.html")

@app.route('/forums')
def forums():
    return render_template("forums.html")

@app.route('/register/')
def register():
    return render_template("login_page/register.html")

@app.route('/login/')
def login():
    return render_template("login_page/login.html")

@app.route('/google_translate/')
def translate():
    return render_template("api_pages/google_translate.html")

# Forums socket.io code
# @socketio.on('testing')
# def handle_message(data):
#     print('received message: ' + data)


# if __name__ == '__main__':
#     socketio.run(app)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
