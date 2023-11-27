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
    CARDS = get_amounts()
    return render_template("index.html", CARDS=CARDS)

@app.route("/album", methods=["GET", "POST"])
def album():
    if request.method == "POST":
        print("Post route is working correctly.")

        # grantPack = db.execute("")

        # Execute function to get a random card

        # Add StickerID to the User Stickers table
        CARDS = get_amounts()
        return render_template("pack.html", CARDS=CARDS)
    else:
        
        CARDS = get_amounts()
        
        return render_template("album.html", CARDS=CARDS)

@app.route("/pomodoro")
def pomodoro():
    return redirect("/")

@app.route("/get_random_card")
def get_random_card():

    list = db.execute("SELECT StickerId FROM stickers")

    values = [row['StickerID'] for row in list]
    random_value = random.choice(values)

    new_card = db.execute("SELECT * FROM stickers WHERE StickerId = :random_value", random_value=random_value)
    return jsonify(new_card)

def get_amounts():
    """Get the amount of each card from the database"""
    amounts = db.execute("SELECT StickerId, Amount FROM USER_STICKERS WHERE UserId = :user_id", user_id="1")
    CARDS = {str(item['StickerID']): item['Amount'] for item in amounts}
    return CARDS

@app.route("/give_pack", methods=["POST"])
def give_pack():
    try:
        db.execute("UPDATE USERS SET UnopenedPacks = UnopenedPacks + 1 WHERE ID = :user_id", user_id="1")
        return jsonify({"message": "Packs updated successfully."})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    

# CARDS = {
#     "01": 0,
#     "02": 0,
#     "03": 0
# }