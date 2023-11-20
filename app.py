from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

CARDS = {
    "01": 1,
    "02": 0,
    "03": 2
}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", CARDS=CARDS)

@app.route("/album")
def album():
    return render_template("album.html", CARDS=CARDS)

@app.route("/pomodoro")
def pomodoro():
    return redirect("/")

@app.route("/get_random_card")
def get_random_card():
    card = {
        'id': 1,
        'name': 'Cherry Tomatoes',
        'description': "Are you sure these are not fruit?",
        'image_url': '/static/01.gif'
    }
    return jsonify(card)