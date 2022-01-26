# import "packages" from flask
import requests, json
from __init__ import app

from tkinter import *

from flask import Flask, request, Blueprint, render_template
from flask_socketio import SocketIO
from image import image_data
from pathlib import Path
from crud.app_crud import app_crud
from crud.app_crud_api import app_crud_api


app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

# create a Flask instance
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)


# connects default URL to render index.html

# The code below creates the default pages that we have hidden from view on our website


@app.route('/')
def mainpage():
    return render_template("main_page.html")


@app.route('/forums')
def forums():
    return render_template("forums.html")


# The code below creates the custom about me pages for each team member
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


@app.route('/bootstrapLayouts/')
def bootstrap_layouts():
    return render_template("our_work/bootstrapLayouts.html")


@app.route('/sci/')
def sci():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": "California ,us", "lat": "0", "lon": "0", "callback": "test", "id": "2172797", "lang": "null",
                   "units": "imperial", "mode": "xml"}

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


@app.route('/api_collection/')
def api_collection():
    # API 1 - Brightest Stars Information
    url1 = "https://brightest-stars.p.rapidapi.com/brightstars"
    headers1 = {
    'x-rapidapi-host': "brightest-stars.p.rapidapi.com",
    'x-rapidapi-key': "21f1126bdamsh1578fd326fc88e5p1b4740jsn5ffba868400c"
    }
    response1 = requests.request("GET", url1, headers=headers1)
    text = response1.json()
    star1name = text[0]['name']
    star1distance = text[0]['distance']
    star1vismag = text[0]['visualMagnitude']
    star2name = text[1]['name']
    star2distance = text[1]['distance']
    star2vismag = text[1]['visualMagnitude']
    star3name = text[2]['name']
    star3distance = text[2]['distance']
    star3vismag = text[2]['visualMagnitude']
    # API 2 - Weather API
    url2 = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring2_1 = {"q":"San Diego"}
    querystring2_2 = {"q":"New York City"}
    querystring2_3 = {"q":"Moscow"}
    headers2 = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "21f1126bdamsh1578fd326fc88e5p1b4740jsn5ffba868400c"}
    response2_1 = requests.request("GET", url2, headers=headers2, params=querystring2_1)
    response2_2 = requests.request("GET", url2, headers=headers2, params=querystring2_2)
    response2_3 = requests.request("GET", url2, headers=headers2, params=querystring2_3)
    text2_1 = response2_1.json()
    text2_2 = response2_2.json()
    text2_3 = response2_3.json()
    city_name = text2_1['location']['name']
    temp = text2_1['current']['temp_f']
    desc = text2_1['current']['condition']['text']
    city_name2 = text2_2['location']['name']
    temp2 = text2_2['current']['temp_f']
    desc2 = text2_2['current']['condition']['text']
    city_name3 = text2_3['location']['name']
    temp3 = text2_3['current']['temp_f']
    desc3 = text2_3['current']['condition']['text']
    # # API 3 - COVID Information
    url3 = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
    querystring3_1 = {"country":"US"}
    querystring3_2 = {"country":"Canada"}
    querystring3_3 = {"country":"Mexico"}
    headers3 = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "21f1126bdamsh1578fd326fc88e5p1b4740jsn5ffba868400c"}
    response3_1 = requests.request("GET", url3, headers=headers3, params=querystring3_1)
    response3_2 = requests.request("GET", url3, headers=headers3, params=querystring3_2)
    response3_3 = requests.request("GET", url3, headers=headers3, params=querystring3_3)
    text3_1 = response3_1.json()
    text3_2 = response3_2.json()
    text3_3 = response3_3.json()
    country1 = text3_1['data']['location']
    cases1 = text3_1['data']['confirmed']
    deaths1 = text3_1['data']['deaths']
    country2 = text3_2['data']['location']
    cases2 = text3_2['data']['confirmed']
    deaths2 = text3_2['data']['deaths']
    country3 = text3_3['data']['location']
    cases3 = text3_3['data']['confirmed']
    deaths3 = text3_3['data']['deaths']
    return render_template("api_pages/api_collection.html", text=text, s1n=star1name, s1d=star1distance, s1vm=star1vismag, s2n=star2name, s2d=star2distance, s2vm=star2vismag, s3n=star3name, s3d=star3distance, s3vm=star3vismag,
                           temp=temp, desc=desc, temp2=temp2, desc2=desc2, temp3=temp3, desc3=desc3, cn1=city_name, cn2=city_name2, cn3=city_name3,
                           text2=text2_1, text3_1=text3_1, text3_2=text3_2, text3_3=text3_3, con1=country1, cases1=cases1, d1=deaths1, con2=country2, cases2=cases2, d2=deaths2, con3=country3, cases3=cases3, d3=deaths3)


@app.route('/quizlet_api/')
def quizlet_api():
    return render_template("api_pages/quizlet.html")


#
#
#
# ALL APP ROUTES BELOW ARE FOR OLD PAGES WE DON'T CURRENTLY USE
# WE CAN DELETE THEM OR KEEP THEM TO ACCESS RUNTIME OF PAGES
#
#
#

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


# Forums socket.io code
# @socketio.on('testing')
# def handle_message(data):
#     print('received message: ' + data)


# if __name__ == '__main__':
#     socketio.run(app)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
