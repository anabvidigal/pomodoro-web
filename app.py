from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///cards.db")

# Prevent caching
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

CARDS = {
    "01": 0,
    "02": 0,
    "03": 0
}

hasUnopenedPack = False

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", CARDS=CARDS)

@app.route("/album", methods=["GET", "POST"])
def album():
    if request.method == "POST":
        print("Post route is working correctly.")
        hasUnopenedPack = True
        # Tell db that the user has a new unopened sticker pack
        # Execute function to get a random card
        # Add StickerID to the User Stickers table
        return render_template("album.html", CARDS=CARDS, pack=hasUnopenedPack)
    else:
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