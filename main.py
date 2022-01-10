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
def mainpage():
    return render_template("main_page.html")


@app.route('/game')
def gamepage():
    return render_template("game.html")


# The code below creates the custom about me pages for each team member

@app.route('/jakub/')
def jakub():
    # response = requests.get("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key"
    #                         "=4E07A0ABAE258C00B17B9EBDEE265FE0&steamid=76561198988285392")
    # API REMAINS COMMENTED OUT SO THAT JAKUB.HTML CAN WORK WITHOUT A VPN
    # text = response.json()
    # game1 = text['response']['games'][0]['name']
    # game1time = str(round(text['response']['games'][0]['playtime_2weeks']/60, 1))
    # game1timeTotal = str(round(text['response']['games'][0]['playtime_forever']/60, 1))
    # game1img = text['response']['games'][0]['img_logo_url']
    # game1ID = text['response']['games'][0]['appid']
    # game2 = text['response']['games'][1]['name']
    # game2time = str(round(text['response']['games'][1]['playtime_2weeks']/60, 1))
    # game2timeTotal = str(round(text['response']['games'][1]['playtime_forever']/60, 1))
    # game2img = text['response']['games'][1]['img_logo_url']
    # game2ID = text['response']['games'][1]['appid']
    # game3 = text['response']['games'][2]['name']
    # game3time = str(round(text['response']['games'][2]['playtime_2weeks']/60, 1))
    # game3timeTotal = str(round(text['response']['games'][2]['playtime_forever']/60, 1))
    # game3img = text['response']['games'][2]['img_logo_url']
    # game3ID = text['response']['games'][2]['appid']
    return render_template("about_us/jakub.html")
    # return render_template("about_us/jakub.html", text=text, g1=game1, g1t=game1time, g1img=game1img,
    #                        g1tT=game1timeTotal, g1ID=game1ID, g2=game2, g2t=game2time, g2tT=game2timeTotal,
    #                        g2ID=game2ID, g2img=game2img, g3=game3, g3t=game3time, g3tT=game3timeTotal,
    #                        g3ID=game3ID, g3img=game3img)


@app.route('/kevin/', methods=['GET', 'POST'])
def kevin():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': "7c1d894378mshb7e7e6c6ecac61bp1f2fcbjsn264b46c0ce80"
    }

    response = requests.request("GET", url, headers=headers)

    text = response.text
    return render_template("about_us/kevin.html", text=text)


@app.route('/tristan/', methods=['GET', 'POST'])
def tristan():
    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "deb5e7f2d3mshad8ffd0c6263400p144918jsnd5cede3b7ac9"
    }

    response = requests.request("GET", url, headers=headers)
    text = response.text
    return render_template("about_us/tristan.html", text=text)


@app.route('/sreeja/', methods=['GET', 'POST'])
def sreeja():
    url = "https://brooklyn-nine-nine-quotes.p.rapidapi.com/api/v1/quotes/random"

    headers = {
        'x-rapidapi-host': "brooklyn-nine-nine-quotes.p.rapidapi.com",
        'x-rapidapi-key': "05cd5ecb69msh65f30850019e80dp124961jsn1cec22cef625"
    }
    response = requests.request("GET", url, headers=headers)

    text = response.text
    return render_template("about_us/sreeja.html", text=text)


@app.route('/hamza/', methods=['GET', 'POST'])
def hamza():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = "{\"key1\": \"value\",\"key2\": \"value\"}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "6aa5930ddamsh4e21c56a3045ce9p1aaf49jsn2e14280f30bb"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    text = response.text
    return render_template("about_us/hamza.html", text=text)


# The code below creates the lab pages

@app.route('/lab1/', methods=['GET', 'POST'])
def greet5():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_workOLD/lab1.html", name=name)
    # starting and empty input default
    return render_template("our_workOLD/lab1.html", name="World")


@app.route('/lab2/')
def lab2():
    return render_template("our_workOLD/lab2.html")


@app.route('/lab3/', methods=['GET', 'POST'])
def lab3():
    path = Path(app.root_path) / "static" / "assets"
    return render_template("our_workOLD/lab3.html", images=image_data(path))


@app.route('/lab4/', methods={'GET', 'POST'})
def lab4():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_workOLD/lab4.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_workOLD/lab4.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/lab4_colorCode/', methods={'GET', 'POST'})
def lab4_colorcode():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_workOLD/lab4_colorCode.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_workOLD/lab4_colorCode.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=24)


@app.route('/lab4_unsignedAdd/')
def lab4_unsignedadd():
    return render_template("our_workOLD/lab4_unsignedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/lab4_signedAdd/')
def lab4_signedadd():
    return render_template("our_workOLD/lab4_signedAdd.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=16, )


@app.route('/tpts/')
def tpts():
    return render_template("our_workOLD/tpts.html")


@app.route('/hackathontt3/', methods={'GET', 'POST'})
def tt3():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("our_workOLD/hackathontt3.html", BITS=int(name))
    # starting and empty input default
    return render_template("our_workOLD/hackathontt3.html", imgBulbOn="/static/assets/bulb_on.gif",
                           imgBulbOff="/static/assets"
                                      "/bulb_off.png",
                           msgTurnOn="Turn On", msgTurnOff="Turn Off", BITS=8)


@app.route('/wireframe/')
def wireframe():
    return render_template("our_workOLD/wireframe.html")


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


@app.route('/bootstrapLayouts/')
def bootstrapLayouts():
    return render_template("our_work/bootstrapLayouts.html")


@app.route('/sci/')
def sci():

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"California ,us","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "7c1d894378mshb7e7e6c6ecac61bp1f2fcbjsn264b46c0ce80"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    text = response.text
    return render_template("class_topics/sci.html", text=text)

    

@app.route('/history/')
def history():
    return render_template("class_topics/history.html")


@app.route('/math/')
def math():
    return render_template("class_topics/math.html")


@app.route('/lit/')
def lit():
    return render_template("class_topics/lit.html")


@app.route('/crud/')
def crud():
    return render_template("homepagestuff/crud.html")


@app.route('/miniquizzes/')
def miniq():
    return render_template("class_topics/miniquizzes.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
