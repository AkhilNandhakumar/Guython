# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/main_page')
def mainpage():
    return render_template("main_page.html")


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
    return render_template("jakub.html")


@app.route('/jakub/', methods=['GET', 'POST'])
def greet0():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("jakub.html", name=name)
    # starting and empty input default
    return render_template("jakub.html", name="World")


@app.route('/anika/', methods=['GET', 'POST'])
def greet1():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("anika.html", name=name)
    # starting and empty input default
    return render_template("anika.html", name="World")


@app.route('/tristan/', methods=['GET', 'POST'])
def greet2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("tristan.html", name=name)
    # starting and empty input default
    return render_template("tristan.html", name="World")


@app.route('/vunsh/', methods=['GET', 'POST'])
def greet3():
    return render_template("index.html")


@app.route('/lab1/', methods=['GET', 'POST'])
def greet5():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("lab1.html", name=name)
    # starting and empty input default
    return render_template("lab1.html", name="World")


@app.route('/lab2/')
def lab2():
    return render_template("lab2.html")


@app.route('/lab3/')
def lab3():
    return render_template("lab3.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.method == "POST":
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


@app.route('/weather1/')
def weather1():
    return render_template("weather1.html")


@app.route('/weather2/')
def weather2():
    return render_template("weather2.html")


@app.route('/weather3/')
def weather3():
    return render_template("weather3.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
