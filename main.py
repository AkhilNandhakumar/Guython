# import "packages" from flask
import requests, json

from tkinter import *

from flask import Flask, render_template, request
from flask import Blueprint, render_template
from image import image_data
from pathlib import Path

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html

# The code below creates the default pages that we have hidden from view on our website

@app.route('/')
def index():
    response = requests.get(
        "https://api.weatherbit.io/v2.0/current?lat=33.0167&lon=117.1115&key=eeb67b06f33d4a3db7ae9df9d3518f4d")
    text = response.json()
    temp = text["data"][0]["temp"]
    imagee = text["data"][0]["weather"]["icon"]
    final = str(temp) + "°C"
    ffinal = str(temp * 9 / 5 + 32) + "°F"
    img = "https://www.weatherbit.io/static/img/icons/" + imagee + ".png"

    return render_template("main_page.html", temp=final, tempf=ffinal, image=img)


@app.route('/main_page')
def mainpage():
    response = requests.get(
        "https://api.weatherbit.io/v2.0/current?lat=33.0167&lon=117.1115&key=eeb67b06f33d4a3db7ae9df9d3518f4d")
    text = response.json()
    temp = text["data"][0]["temp"]
    final = str(temp) + "°C"
    return render_template("main_page.html", temp=final)


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("about_us/jakub.html")


# The code below creates the custom about me pages for each team member

@app.route('/jakub/', methods=['GET', 'POST'])
def greet0():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about_us/jakub.html", name=name)
    # starting and empty input default
    return render_template("about_us/jakub.html", name="World")


@app.route('/anika/', methods=['GET', 'POST'])
def greet1():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about_us/anika.html", name=name)
    # starting and empty input default
    return render_template("about_us/anika.html", name="World")


@app.route('/tristan/', methods=['GET', 'POST'])
def greet2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about_us/tristan.html", name=name)
    # starting and empty input default
    return render_template("about_us/tristan.html", name="World")


@app.route('/vunsh/', methods=['GET', 'POST'])
def greet3():
    return render_template("about_us/vunsh.html")


# The code below creates the lab pages

@app.route('/lab1/', methods=['GET', 'POST'])
def greet5():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab1.html", name=name)
    # starting and empty input default
    return render_template("our_work/lab1.html", name="World")


@app.route('/lab2/')
def lab2():
    return render_template("our_work/lab2.html")


@app.route('/lab3/', methods=['GET', 'POST'])
def lab3():
    path = Path(app.root_path) / "static" / "assets"
    return render_template("our_work/lab3.html", images=image_data(path))


@app.route('/lab4/', methods={'GET', 'POST'})
def lab4():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab4.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/lab4.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/lab4_colorCode/', methods={'GET', 'POST'})
def lab4_colorcode():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/lab4_colorCode.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/lab4_colorCode.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=24)


@app.route('/lab4_unsignedAdd/')
def lab4_unsignedadd():
    return render_template("our_work/lab4_unsignedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/lab4_signedAdd/')
def lab4_signedadd():
    return render_template("our_work/lab4_signedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/tpts/')
def tpts():
    return render_template("our_work/tpts.html")


@app.route('/hackathontt3/', methods={'GET', 'POST'})
def tt3():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_work/hackathontt3.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_work/hackathontt3.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/wireframe/')
def wireframe():
    return render_template("our_work/wireframe.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.method == "POST":
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


# The code below creates the weather pages

@app.route('/weather1/')
def weather1():
    return render_template("weather_info/weather1.html")


@app.route('/weather2/')
def weather2():
    return render_template("weather_info/weather2.html")


@app.route('/weather3/')
def weather3():
    return render_template("weather_info/weather3.html")


@app.route('/weather4/')
def weather4():
    return render_template("weather_info/weather4.html")


@app.route('/wtd1/')
def wtd1():
    return render_template("weather_info/wtd1.html")


@app.route('/wtd2/')
def wtd2():
    return render_template("weather_info/wtd2.html")


@app.route('/wtd3/')
def wtd3():
    return render_template("weather_info/wtd3.html")


@app.route('/weather_checks/')
def wchecks():
    return render_template("weather_info/weather_checks.html", background='linear-gradient(-45deg, #f3feed, #5c8be4, '
                                                                   '#fbb73a)')


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
