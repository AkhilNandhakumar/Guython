from flask import Blueprint, render_template

app_topics = Blueprint('topics', __name__,
                             url_prefix='/topics',
                             template_folder='templates',
                             static_folder='static',
                             static_url_path='static')


@app_topics.route('/css/')
def css():
    return render_template("topics/css.html")


@app_topics.route('/javascript/')
def javascript():
    return render_template("topics/javascript.html")


@app_topics.route('/html/')
def html():
    return render_template("topics/html.html")

