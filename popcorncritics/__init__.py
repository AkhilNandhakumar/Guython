from flask import Blueprint, render_template

app_popcorn = Blueprint('popcorn', __name__,
                         url_prefix='/popcornpages',
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='static')


@app_popcorn.route('/notes/')
def notes():
    return render_template("popcornpages/notes.html")
