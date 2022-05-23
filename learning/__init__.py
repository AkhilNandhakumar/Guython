from flask import Blueprint, render_template

app_learning = Blueprint('learning', __name__,
                       url_prefix='/learning',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='static')


@app_learning.route('/movie/')
def movies():
    return render_template("learning/movie.html")


@app_learning.route('/starter/')
def starter():
    return render_template("learning/starter.html")


@app_learning.route('/testprep/')
def testprep():
    return render_template("learning/testprep.html")
