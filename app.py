from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from cs50 import SQL
import traceback
import random

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to database
db = SQL("sqlite:///cards.db")

# Prevent caching
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

hasUnopenedPack = False

@app.route("/", methods=["GET", "POST"])
def index():
    amounts = get_amounts()
    return render_template("index.html", amounts=amounts)

@app.route("/album")
def album():

    unopened = get_unopened()
    amounts = get_amounts()

    # Create a function that gets the info of the card
    # Pass amounts parameter
    # Returns a list of dicts?

    return render_template("album.html", amounts=amounts, unopened=unopened)
    

@app.route("/pomodoro")
def pomodoro():
    return redirect("/")

@app.route("/get_random_card")
def get_random_card():

    list = db.execute("SELECT StickerId FROM stickers")

    values = [row['StickerID'] for row in list]
    random_value = random.choice(values)

    new_card = db.execute("SELECT * FROM stickers WHERE StickerId = :random_value", random_value=random_value)
    register_new_card(random_value)

    return jsonify(new_card)

@app.route("/give_pack", methods=["POST"])
def give_pack():
    try:
        db.execute("UPDATE USERS SET UnopenedPacks = UnopenedPacks + 1 WHERE ID = :user_id", user_id="1")
        return jsonify({"message": "Packs updated successfully."})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# Functions
def get_amounts():
    """Get the amount of each card from the database"""
    get_amounts = db.execute("SELECT StickerId, Amount FROM USER_STICKERS WHERE UserId = :user_id", user_id="1")
    amounts = {str(item['StickerID']): item['Amount'] for item in get_amounts}
    return amounts

def get_unopened():
    get_unopened = db.execute("SELECT UnopenedPacks FROM USERS WHERE ID = :user_id", user_id="1")
    unopened = get_unopened[0]['UnopenedPacks']
    return unopened

def register_new_card(stickerId):
    db.execute("UPDATE USER_STICKERS SET Amount = Amount + 1 WHERE StickerID = :stickerId", stickerId=stickerId)
    db.execute("UPDATE USERS SET UnopenedPacks = UnopenedPacks - 1 WHERE ID = :user_id", user_id="1")
