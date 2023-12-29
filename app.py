from flask import Flask, redirect, render_template, jsonify
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
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    amounts = get_amounts()
    return render_template("index.html", amounts=amounts)

@app.route("/album")
def album():

    unopened = get_unopened()
    amounts = get_amounts()
    stickers = get_cards(amounts)
    # [
    #   {'id': 1, 'title': 'Cherry Tomato', 'description': 'You sure theyre not a fruit?'},
    #   {'id': 2, 'title': 'Bloody Mary', 'description': 'This form of tomato is adult-only.'},
    #   {'id': 3, 'title': 'Bruschetta', 'description': 'Tomato finger food.'}
    # ]

    return render_template("album.html", amounts=amounts, unopened=unopened, stickers=stickers)
    

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


def get_cards(amounts):

    cards = []

    print(f"Parameter passed into get_cards function: {amounts}")

    for key, value in amounts.items():
        print(f"Key: {key}")
    
        print(f"Value: {value}")
        get_card = db.execute("SELECT * FROM STICKERS WHERE StickerId = :sticker_id", sticker_id=key)

        for row in get_card:
            id = row['StickerID']
            amount = value
            title = row['Title']
            description = row['Description']
            cards.append({'id': id, 'amount': amount, 'title': title, 'description': description})

    print(cards)        
    return cards
        
    

def get_unopened():
    get_unopened = db.execute("SELECT UnopenedPacks FROM USERS WHERE ID = :user_id", user_id="1")
    unopened = get_unopened[0]['UnopenedPacks']
    return unopened

def register_new_card(stickerId):
    db.execute("UPDATE USER_STICKERS SET Amount = Amount + 1 WHERE StickerID = :stickerId", stickerId=stickerId)
    db.execute("UPDATE USERS SET UnopenedPacks = UnopenedPacks - 1 WHERE ID = :user_id", user_id="1")
