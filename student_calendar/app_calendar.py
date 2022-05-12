from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_login import login_required, logout_user

from cruddy.query import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_calendar = Blueprint('calendar', __name__,
                         url_prefix='/calendar',
                         template_folder='templates/calendar/',
                         static_folder='static',
                         static_url_path='static')


@app_calendar.route('/')
@app_calendar.route('/student/')
@login_required
def student():
    return render_template("student.html")


@app_calendar.route('/admin/')
@login_required
def admin():
    return render_template("admin.html")



