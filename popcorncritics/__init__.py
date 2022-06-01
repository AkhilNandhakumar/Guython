import os
from __init__ import app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import requests

import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cruddy.query import user_by_id
from cruddy.model import Notes
from uploady.app_upload import upload_save

from cruddy.query import user_by_id

app_popcorn = Blueprint('popcorn', __name__,
                         url_prefix='/popcornpages',
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='static')

@app_popcorn.route('/random')
def random():
    return render_template("popcornpages/random.html")
    configR = (requests.get("https://api.themoviedb.org/3/configuration?api_key=16165f36aebaa78f40ee87f1bf743c44")).json()
    topR = (requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
    id_listR = []
    x = 0
    while x < 100:
        id = topR["results"][x]["id"]
        id_listR.append(id)
        x += 1
    list = []
    for x in id_listR:
        details = (requests.get("https://api.themoviedb.org/3/movie/" + str(x) + "?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
        n_dict = {}
        n_dict["title"] = details["title"]
        n_dict["image"] = configR["images"]["secure_base_url"] + "w342" + details["poster_path"]
        list.append(n_dict)
    return render_template("popcornpages/random.html", list=list)


@app_popcorn.route('/top')
def top():
    id_list = []
    config = (requests.get("https://api.themoviedb.org/3/configuration?api_key=16165f36aebaa78f40ee87f1bf743c44")).json()
    top = (requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US&page=1")).json()
    x = 0
    while x < 10:
        id = top["results"][x]["id"]
        id_list.append(id)
        x += 1

    d_list = []
    for id in id_list:
        d_json = (requests.get("https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
        n_dict = {}
        n_dict["genre"] = d_json["genres"][0]["name"]
        n_dict["caption"] = d_json["overview"]
        n_dict["country"] = d_json["production_countries"][0]["name"]
        n_dict["date"] = d_json["release_date"]
        n_dict["runtime"] = d_json["runtime"]
        n_dict["tagline"] = d_json["tagline"]
        n_dict["title"] = d_json["title"]
        n_dict["rating"] = d_json["vote_average"]
        n_dict["image"] = config["images"]["secure_base_url"] + "w185" + d_json["poster_path"]
        d_list.append(n_dict)
    return render_template("popcornpages/top.html", d_list=d_list)

@app_popcorn.route('/topL')
def topL():
    topL = (requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US&page=1")).json()
    d_jsonL = (requests.get("https://api.themoviedb.org/3/movie/" + str(topL["results"][14]["id"]) + "?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
    configL = (requests.get("https://api.themoviedb.org/3/configuration?api_key=16165f36aebaa78f40ee87f1bf743c44")).json()
    movie = {}
    movie["title"] = d_jsonL["title"]
    movie["tagline"] = d_jsonL["tagline"]
    movie["genre"] = d_jsonL["genres"][0]["name"]
    movie["caption"] = d_jsonL["overview"]
    movie["country"] = d_jsonL["production_countries"][0]["name"]
    movie["date"] = d_jsonL["release_date"]
    movie["runtime"] = d_jsonL["runtime"]
    movie["rating"] = d_jsonL["vote_average"]
    movie["image"] = configL["images"]["secure_base_url"] + "w185" + d_jsonL["poster_path"]
    return render_template("popcornpages/topL.html", movie=movie)

@app_popcorn.route('/notes/')
def notes():
    user = ""
    list_notes = []
    return render_template("popcornpages/notes.html", user=user, notes=list_notes)

@app_popcorn.route('/notes2/')
def notes2():
    user = ""
    list_notes = []
    return render_template("popcornpages/notes2.html", user=user, notes=list_notes)

@app_popcorn.route('/notesL/')
def notesL():
    return render_template("popcornpages/notesL.html")

@app_popcorn.route('/nowplaying')
def nowplaying():
    id_listNP = []
    configNP = (requests.get("https://api.themoviedb.org/3/configuration?api_key=16165f36aebaa78f40ee87f1bf743c44")).json()
    nowplaying = (requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US&page=1")).json()
    x = 0
    while x < 10:
        idNP = nowplaying["results"][x]["id"]
        id_listNP.append(idNP)
        x += 1

    NP_list = []
    for idNP in id_listNP:
        NP_json = (requests.get("https://api.themoviedb.org/3/movie/" + str(idNP) + "?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
        NP_dict = {}
        NP_dict["genre"] = NP_json["genres"][0]["name"]
        NP_dict["caption"] = NP_json["overview"]
        NP_dict["country"] = NP_json["production_countries"][0]["name"]
        NP_dict["date"] = NP_json["release_date"]
        NP_dict["runtime"] = NP_json["runtime"]
        NP_dict["tagline"] = NP_json["tagline"]
        NP_dict["title"] = NP_json["title"]
        NP_dict["rating"] = NP_json["vote_average"]
        NP_dict["image"] = configNP["images"]["secure_base_url"] + "w185" + NP_json["poster_path"]
        NP_list.append(NP_dict)
    return render_template("popcornpages/nowplaying.html", NP_list=NP_list)

@app_popcorn.route('/nowplayingL')
def nowplayingL():
    nowplayingL = (requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US&page=1")).json()
    d_jsonNPL = (requests.get("https://api.themoviedb.org/3/movie/" + str(nowplayingL["results"][14]["id"]) + "?api_key=16165f36aebaa78f40ee87f1bf743c44&language=en-US")).json()
    configNPL = (requests.get("https://api.themoviedb.org/3/configuration?api_key=16165f36aebaa78f40ee87f1bf743c44")).json()
    movieNP = {}
    movieNP["title"] = d_jsonNPL["title"]
    movieNP["tagline"] = d_jsonNPL["tagline"]
    movieNP["genre"] = d_jsonNPL["genres"][0]["name"]
    movieNP["caption"] = d_jsonNPL["overview"]
    movieNP["country"] = d_jsonNPL["production_countries"][0]["name"]
    movieNP["date"] = d_jsonNPL["release_date"]
    movieNP["runtime"] = d_jsonNPL["runtime"]
    movieNP["rating"] = d_jsonNPL["vote_average"]
    movieNP["image"] = configNPL["images"]["secure_base_url"] + "w185" + d_jsonNPL["poster_path"]
    return render_template("popcornpages/nowplayingL.html", movie=movieNP)

