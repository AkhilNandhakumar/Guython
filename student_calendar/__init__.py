from flask import Blueprint, render_template

app_nhcalendar = Blueprint('calendar', __name__,
                       url_prefix='/calendar',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='static')


@app_nhcalendar.route('/student/')
def student():
    return render_template("calendar/student.html")


@app_nhcalendar.route('/admin/')
def admin():
    return render_template("calendar/admin.html")
