
from flask import Flask
from flask import jsonify, render_template, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/jsnname/<value>')
def jsnname(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/name/<value>')
def name(value):
    return "Hello, " + value + "!"


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)