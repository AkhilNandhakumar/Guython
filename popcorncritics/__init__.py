from flask import Blueprint, render_template
import requests

app_popcorn = Blueprint('popcorn', __name__,
                         url_prefix='/popcornpages',
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='static')


@app_popcorn.route('/notes/')
def notes():
    return render_template("popcornpages/notes.html")

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
    return render_template("popcornpages/topL.html")