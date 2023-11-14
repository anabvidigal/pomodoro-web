from flask import Flask, redirect, render_template, request, session
from flask_session import Session
# import sqlite3

# conn = sqlite3.connect('cards.db')

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session for filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

CARDS = {
    "01": 0,
    "02": 0,
    "03": 0
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