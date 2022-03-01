import requests
from flask import Blueprint, render_template

app_classtopics = Blueprint('class_topics', __name__,
                             url_prefix='/class_topics',
                             template_folder='templates',
                             static_folder='static',
                             static_url_path='static')


@app_classtopics.route('/sci/')
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


@app_classtopics.route('/history')
def history():
    return render_template("class_topics/history.html")


@app_classtopics.route('/math')
def math():
    return render_template("class_topics/math.html")


@app_classtopics.route('/lit')
def lit():
    return render_template("class_topics/lit.html")


@app_classtopics.route('/periodictable')
def periodictable():
    url = "https://periodictable.p.rapidapi.com/"
    headers = {
        'x-rapidapi-host': "periodictable.p.rapidapi.com",
        'x-rapidapi-key': "21f1126bdamsh1578fd326fc88e5p1b4740jsn5ffba868400c"}
    response = requests.request("GET", url, headers=headers)
    text = response.json()
    return render_template("class_topics/periodictable.html", text=text)


