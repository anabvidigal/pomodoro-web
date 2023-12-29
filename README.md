# PomoAlbum
#### Video Demo:  <https://www.loom.com/share/f033bbe1889340d5a03100bbd6cb0446?sid=755746b0-80ca-4731-9023-c82c5fa69eff>
#### Description
PomoAlbum is a fullstack web-app developed for CS50's final project.  
Complete timers and earn tomato-themed collectibles to have in your album!  

## Technologies
PomoAlbum was developed using Python, JavaScript, Flask, Jinja, SQLite3, HTML, CSS and Bootstrap.  

Flask handles the routes for the application, and the project uses the templates structure. JavaScript handles events and makes HTTP requests for the back-end, running with the Flask server and the SQLite3 database.  

This choice of structure allows the application to grow and change easily in the future, with the modular nature of Flask routes and templates.

## Structure
In the root folder, there's the app.py file for the Python/Flask server; the cards.db, which is the file used by SQLite3 for the database; this README.md and a schema.md file, which is a cheatsheet for quick access for frequent and useful commands for the SQLite3.

### Flask server
The routes I have in the Flask server are

* /
* /album
* /pomodoro
* /get_random_card
* /give_pack

### Database
The database is in the *cards.db* file, and runs in SQLite3. Its schema includes:

* Stickers
  * StickerID, Title, Description, Image;
* User_Stickers
  * UserId, StickerID;
* Users
  * ID, Username, UnopenedPacks

### Templates
Inside the templates folder, there are three files:

* album.html
  * Layouts the album view, which loops over existing total stickers and populates them according to the user's earned stickers.
* index.html
  * Layouts the homepage, with the pomodoro timer.
* layout.html
  * Has the overall common code throughout the whole application, such as head and meta tags, as well as the navigation menu.

### Static
In the static folder there are JavaScript files, the CSS stylesheet, images and the icon file.

#### JavaScript

##### script.js
* Creates the timer for the 25 minutes;
* Handles the start, pause and reset actions for the timer;
* When the timer runs out, executes givePack, which sends an HTTP request to the Flask server to add an unopened sticker pack to that user;
* Shows a card to make clear to the user that they can open their new sticker pack in the album.

##### album.js
* Checks if the user has unopened sticker packs, and if they do, shows a modal with the functionality of opening packs;
* Sends a HTTP request for the back-end, fetching the get_random_card function;
* Populates the modal with information on the new random sticker that was granted to the user;
* Adds a confetti effect when a new pack is opened (imported from a third-party library);
* Refreshes the page after a new sticker was earned, so it can be seen in the album.

#### CSS
In the CSS I've implemented the flipping functionality of stickers in the album, using *transform*, *z-index* and *backface-visibility*.

