from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from datetime import datetime
import calendar

from student_calendar.cal_query import *

app_calendar = Blueprint('calendar', __name__,
                         url_prefix='/calendar',
                         template_folder='templates/calendar/',
                         static_folder='static',
                         static_url_path='static')


@app_calendar.route('/')
def student():
    currentday = datetime.now().day
    monthnum = datetime.now().month
    currentmonth = calendar.month_name
    currentyear = datetime.now().year
    days_list = []
    len_days = len(users_all())
    calevent = []
    year = []
    month = []
    for x in range(len(users_all())):
        calevent.append(users_all()[x]['event'])
        year.append(str(users_all()[x]['yearmonth'])[0:4])
        days_list.append(str(users_all()[x]['day']))
        if str(users_all()[x]['yearmonth'])[5:6] == "0":
            month.append(str(users_all()[x]['yearmonth'])[6:7])
        else:
            month.append(str(users_all()[x]['yearmonth'])[5:7])
    return render_template("student.html", table=users_all(), days_list=days_list,
                           len_days=len_days, calevent=calevent, year=year, month=month, monthnum=monthnum,
                           currentday=currentday, currentmonth=currentmonth, currentyear=currentyear)


@app_calendar.route('/admin/')
@login_required
def admin():
    currentday = datetime.now().day
    monthnum = datetime.now().month
    currentmonth = calendar.month_name
    currentyear = datetime.now().year
    days_list = []
    len_days = len(users_all())
    calevent = []
    year = []
    month = []
    for x in range(len(users_all())):
        calevent.append(users_all()[x]['event'])
        year.append(str(users_all()[x]['yearmonth'])[0:4])
        days_list.append(str(users_all()[x]['day']))
        if str(users_all()[x]['yearmonth'])[5:6] == "0":
            month.append(str(users_all()[x]['yearmonth'])[6:7])
        else:
            month.append(str(users_all()[x]['yearmonth'])[5:7])
    return render_template("admin.html", table=users_all(), days_list=days_list,
                           len_days=len_days, calevent=calevent, year=year, month=month, monthnum=monthnum,
                           currentday=currentday, currentmonth=currentmonth, currentyear=currentyear)


@app_calendar.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Calendar(
            request.form.get("name"),
            request.form.get("event"),
            request.form.get("day"),
            request.form.get("yearmonth")
        )
        print(po)
        po.create()
    return redirect(url_for('calendar.admin'))


# CRUD read
@app_calendar.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        eventid = request.form.get("eventid")
        po = user_by_event(eventid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    currentday = datetime.now().day
    monthnum = datetime.now().month
    currentmonth = calendar.month_name
    currentyear = datetime.now().year
    days_list = []
    len_days = len(users_all())
    calevent = []
    year = []
    month = []
    for x in range(len(users_all())):
        calevent.append(users_all()[x]['event'])
        year.append(str(users_all()[x]['yearmonth'])[0:4])
        days_list.append(str(users_all()[x]['day']))
        if str(users_all()[x]['yearmonth'])[5:6] == "0":
            month.append(str(users_all()[x]['yearmonth'])[6:7])
        else:
            month.append(str(users_all()[x]['yearmonth'])[5:7])
    return render_template("admin.html", table=table, days_list=days_list,
                           len_days=len_days, calevent=calevent, year=year, month=month, monthnum=monthnum,
                           currentday=currentday, currentmonth=currentmonth, currentyear=currentyear)


@app_calendar.route('/read2/', methods=["POST"])
def read2():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        yearmonth = request.form.get("yearmonth")
        po = user_by_ym(yearmonth)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("admin.html", table=table)


# CRUD update
@app_calendar.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        eventid = request.form.get("eventid")
        name = request.form.get("name")
        event = request.form.get("event")
        day = request.form.get("day")
        yearmonth = request.form.get("yearmonth")
        po = user_by_event(eventid)
        if po is not None:
            po.update(name, event, day, yearmonth)
    return redirect(url_for('calendar.admin'))


# CRUD delete
@app_calendar.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        eventid = request.form.get("eventid")
        print(eventid)
        po = user_by_event(eventid)
        if po is not None:
            po.delete()
    return redirect(url_for('calendar.admin'))



