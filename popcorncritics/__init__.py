from flask import Blueprint, render_template


app_popcorncritics = Blueprint('popcorncritics', __name__,
                       url_prefix='/popcorncritics',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='static')


@app_popcorncritics.route('/popcorn/')
def popcorn():
    return render_template("popcorn.html")

