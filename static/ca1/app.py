"""
My website has 2 types of logged in users.
    - Fans. You must be logged in to place an order, and will have a user page where they can show their collection.
        Login information:
        User ID             DerekBridge
        Password            DerekBridgeSuperFan1

    - Artists. An artist page let's you list releases and update inventory levels. Derek Bridge And The HTML Five currently have no live releases.
        Login information:
        User ID             DerekBridgeAndTheHTMLFive
        Password            DerekBridgeBand1

I do not own all the artwork displayed on this site, but permission has been received from the respective rights holders.
"""

from flask import Flask, render_template, session, redirect, url_for, g, request
from database import get_db, close_db

from flask_session import Session
from forms import LibraryForm, AddToCart, ContactForm, FanLoginForm, FanRegistrationForm, ArtistLoginForm, ArtistRegistrationForm, NewForm

from sqlite3 import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps

from random import choices # We want to use this to choose random releases for our recommendation algorithm

app = Flask(__name__)
app.teardown_appcontext(close_db)

app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False # True would be persistent
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)
    g.state = session.get("state", None) # Also creating a global "state" variable that signifies whether the user is a fan, artist or None

# I have two "login_required" decorators, one for if login is required for a fan and another for if login is required by an artist
def fan_login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("fan_login", next = request.url))
        return view(**kwargs)
    return wrapped_view

def artist_login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("artist_login"))
        return view(**kwargs)
    return wrapped_view





################################ general site stuff ################################ 
# ________________________________________________________________________________________________________________________________________________________________
# HOME

@app.route("/", methods = ["GET", "POST"])
def home():
    """Basic starting programme to display home screen content.
    Creates a session for the user, and gives this user 3 recommendations of records to check out to get them started.
    If a session is already created, these recommendations are based on the genre of the previous purchases or cart content.
    Otherwise, they're completely random."""
    try:
        db = get_db()

        recommendations = db.execute("""
        SELECT * FROM inventory;
        """).fetchall()

        rec_list = choices(recommendations, k = 3)
        
        return render_template("home.html", title = "the depth | An online record store for all things Irish", rec_list = rec_list)

    except:
        return render_template("home.html", title = "ERROR") # Returning title as ERROR is only for me as testing





# ________________________________________________________________________________________________________________________________________________________________
# LIBRARY

@app.route("/library", methods = ["GET", "POST"])
def library():
    """
    A page where you can generally view all releases that are hosted on the site.
    It features a drop down that allows you to only see releases from a specific artist or genre.
    """
    try:
        form = LibraryForm() # We want to call the form that'll be used to present a drop down at the top of the page

        db = get_db()
        options_list = db.execute("""SELECT * FROM inventory;""").fetchall() # Call every release in our inventory into a list of options

        artist_list = [] # Create empty artist list for SelectField

        for line in options_list: # Parse the information for each artist
            if line["artist"] not in artist_list: # include this if to prevent adding in duplicates
                artist_list.append(line["artist"]) # Put just the artist name into the above lit

        artist_list = sorted(artist_list) # Sort this list so that it's alphabetised

        artist_list.insert(0, "ALL RELEASES") # Add an option for "all releases" into the very start of our drop down

        form.artist.choices = artist_list # pass this back to the form's selectfield to populate the options.

        if form.validate_on_submit(): # We want to do all of the previous list processing whether or not the data is validated
            
            selected_artist = form.artist.data # the user has selected an artist to narrow it down to at this point

            if selected_artist != "ALL RELEASES": # If they've selected "ALL RELEASES" we want it to miss the if as it should show all releases then

                display_library = db.execute("""SELECT * FROM inventory WHERE artist = ?;""", (selected_artist, )).fetchall()

                return render_template("library.html", form = form, display_library = display_library, title = selected_artist + "'s releases | the depth")          
        
        display_library = db.execute("""SELECT * FROM inventory;""").fetchall() # if the form didn't validate, we want to show them all releases by default
        return render_template("library.html", form = form, display_library = display_library, title = "All releases | the depth")   

    except:
        return render_template("library.html", form = form, title = "ERROR") # Would reach here if there was an error. IDK what error could make it reach here though.      





# ________________________________________________________________________________________________________________________________________________________________
# ABOUT

@app.route("/about", methods = ["GET", "POST"])
def about():
    """
    Really basic routing to display the contents of the site's 'about' page.
    """
    return render_template("about.html", title = "About | the depth")








# ________________________________________________________________________________________________________________________________________________________________
# COLLECTION

@app.route("/collection/<user_id>", methods = ["GET", "POST"])
def collection(user_id):
    """
    Shows things users have previously ordered.
    Login isn't required here, this is a way for users to show off their purchases - so is visible to anyone, logged in or otherwise.
    """

    db = get_db()

    display_collection = db.execute("""
        SELECT * FROM inventory
        WHERE code =
        (SELECT code FROM collections
        WHERE user_id = ?);
        """, (user_id, )).fetchall() # Select the codes from collections where the user_id matches the user_id from the URL variable, and cross reference these codes to collect all of the info about it from the inventory


    return render_template("collection.html", display_collection = display_collection, title = user_id + "'s collection of purchases | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# ARTIST PAGE ???????????????????? The url of this is proving to be a nightmare to pass around

@app.route("/artist_page/<user_id>", methods = ["GET", "POST"])
def artist_page(user_id):
    """
    Shows all releases by a particular artist on one page.
    Login isn't required here, this is a way for send what they have available for purchase to people, logged in or otherwise.
    """

    db = get_db()

    artist_page = db.execute("""
        SELECT * FROM inventory
        WHERE artist =
        (SELECT artist_name FROM artists
        WHERE user_id = ?);
        """, (user_id, )).fetchall()

    artist = db.execute("""
        SELECT artist_name FROM artists
        WHERE user_id = ?;
        """, (user_id, )).fetchone()

    artist_str = ""
    for i in artist:
        artist_str += i

    return render_template("artist_page.html", artist_page = artist_page, artist = artist_str, title = "artist_str | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# LISTING

@app.route("/listing/<int:code>", methods = ["GET", "POST"])
def listing(code: int):
    """
    A function to return a listing page, customised automatically to display the information from registered artists that have uploaded releases.
    We want all parts of this function to be accessible whether the user is logged in or not.
    If the user is not logged in, we want the "add to cart" button to redirect them to the login page.
    """

    db = get_db()

    release = db.execute("""SELECT * FROM inventory
                            WHERE code = ?""", (code, )).fetchone()

    title = release["title"] + " | " + release["artist"]

    form = AddToCart()

    if form.validate_on_submit():

        quantity = form.quantity.data
    
        if "cart" not in session:
            session["cart"] = {code: 0}

        if code not in session["cart"]:
            session["cart"][code] = quantity
    
        session["cart"][code] = session["cart"][code] + quantity

        return redirect( url_for("cart") )

    return render_template("listing.html", form = form, title = title + " | the depth", release = release)





# ________________________________________________________________________________________________________________________________________________________________
# LOGOUT

@app.route("/logout")
def logout():
    session.clear()
    return redirect (url_for( "home" ))





################################ fan user specific ################################ 
# ________________________________________________________________________________________________________________________________________________________________
# FAN LOGIN

@app.route("/fan_login", methods = ["GET", "POST"])
def fan_login():
    """
    A function for logging into a fan account.
    This page shouldn't be navigable to for users that are already logged in.
    """

    form = FanLoginForm()

    if form.validate_on_submit():

        user_id = form.user_id.data
        password = form.password.data

        db = get_db()

        matching_users = db.execute(
            """
            SELECT * FROM fans
            WHERE user_id = ?;
            """,
            (user_id,)
        ).fetchone()

        if matching_users is None: # user id isn't in matching users, return that as an error
            form.user_id.errors.append("This user ID is not registered with us")

        elif not check_password_hash(matching_users["password"], password):
            form.password.errors.append("Password invalid")

        else: # Password & user id must match, so log them in.
            
            # session.clear()
            # Don't clear the session here, store where they are before logging in to the session, their cart contents etc so that they can be ridrected back after being logged in 

            session["user_id"] = user_id
            session["state"] = "fan"

            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("home")
            return redirect(next_page)

    return render_template("fan_login.html", form = form, title = "Fan Login | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# FAN REGISTRATION

@app.route("/fan_registration", methods = ["GET", "POST"])
def fan_registration():
    """
    A function for registering as a new user.
    """

    form = FanRegistrationForm()

    if form.validate_on_submit():

        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data

        db = get_db()

        try:
            db.execute(
            """
            INSERT INTO fans (user_id, password)
            VALUES (?, ?);
            """,
            (user_id, generate_password_hash(password))  
            )
            db.commit()

            return redirect( url_for( "fan_login" ) )
        
        except IntegrityError:
            form.user_id.errors.append("User ID is already taken")
    
    return render_template("fan_registration.html", form = form, title = "Fan Registration | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# CART ???????????? Not populating or sending across the required info but no errors.
# Hitting the "order" button should reduce the stock of that release by the quantity in the cart

@app.route("/cart", methods = ["GET", "POST"])
@fan_login_required
def cart():
    """
    A cart to collate the fans cart contents into one handy endpoint.
    """

    message = ""

    db = get_db()

    total = 0.0

    if "cart" not in session:
        session["cart"] = {}
    
    if len(session["cart"]) == 0:
        message = "Your cart is empty. Why not check out our library to get started adding releases to your cart!"

    fleshed_cart = {}

    for item in session["cart"]:
        item = db.execute(
            """
            SELECT title FROM inventory WHERE code = ?;
            """, (item,)).fetchone

    return render_template("cart.html", title = "Your shopping cart | the depth", cart = session["cart"], total = total, message = message)





################################ artist user specific ################################ 
# ________________________________________________________________________________________________________________________________________________________________
# ARTIST LOGIN

@app.route("/artist_login", methods = ["GET", "POST"])
def artist_login():
    """
    A function for logging into an artist account.
    """

    form = ArtistLoginForm()

    if form.validate_on_submit():

        user_id = form.user_id.data
        password = form.password.data

        db = get_db()

        matching_users = db.execute(
            """
            SELECT * FROM artists
            WHERE user_id = ?;
            """,
            (user_id,)
        ).fetchone()

        if matching_users is None: # user id isn't in matching users, return that as an error
            form.user_id.errors.append("This user ID is not registered with us")

        elif not check_password_hash(matching_users["password"], password):
            form.password.errors.append("Password invalid")

        else: # Password & user id must match, so log them in.

            session["user_id"] = user_id
            session["state"] = "artist"
            return redirect( url_for( "home" ) )

    return render_template("artist_login.html", form = form, title = "Artist Login | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# ARTIST REGISTRATION

@app.route("/artist_registration", methods = ["GET", "POST"])
def artist_registration():
    """
    A function for registering as a new user.
    """

    form = ArtistRegistrationForm()

    if form.validate_on_submit():

        user_id = form.user_id.data
        artist_name = form.artist_name.data
        password = form.password.data
        password2 = form.password2.data

        db = get_db()

        try:
            db.execute(
            """
            INSERT INTO artists (user_id, artist_name, password)
            VALUES (?, ?, ?);
            """,
            (user_id, artist_name, generate_password_hash(password))  
            )
            db.commit()

            return redirect( url_for( "artist_login" ) )
        
        except IntegrityError:
            form.user_id.errors.append("User ID is already taken")

    return render_template("artist_registration.html", form = form, title = "Artist Registration | the depth")





# ________________________________________________________________________________________________________________________________________________________________
# NEW RELEASE

@app.route("/new", methods = ["GET", "POST"])
@artist_login_required
def new():
    """
    A routing function for logged in artists to add new releases to the database of products for sale.
    """

    form = NewForm() # Have to put the form outside the try / except as we still want to call the form if there's an exception

    # This form shouldn't be accessible if they're not - and we'll take artist name to add to db from there.
    # I think this should also be the only session check we need to do.

    outcome = ""

    if form.validate_on_submit(): # If the request is a POST request and that data is validated, then there is a catch it here
        
        db = get_db()

        artist = db.execute("""SELECT artist_name FROM artists WHERE user_id = ?;""", (g.user, )).fetchone() # The artist of the release will always be the same, as it'll be the logged in user

        artist_format = ""

        for i in artist:
            artist_format += i


        title = str(form.title.data) # It doesn't matter if this is already in the database as this can be true of a few releases
        if title == "": # If title is left blank, we don't want to send an error, instead we want to default change that to "Untitled"
            title = "Untitled"

        format = str(form.format.data) # I don't think there are any checks we want to do with the format, but we will want to store it.

        price = float(form.price.data) # If price = 0 but format is not digital, we need to send an error
        if price <= 0:
            form.price.errors.append("You need to charge something for your release")

        stock = int(form.stock.data)
        if stock <= 0:
            form.stock.errors.append("You must have at least 1 of the item available for sale in order to list on the depth")

        genre = str(form.genre.data) # I don't think there are any checks we want to do with the genre outside of what's validated from the forms.py, but we will want to store it.
        if genre == None:
            form.stock.errors.append("Inputting a genre will help us to get your release in front of the right fans")

        # artwork = form.artwork.data <---- come back to this
        artwork = "invalid_artwork.jpg"

        # At this stage we want to call the database and check if the release is already there.

        potential_conflicts = db.execute("""SELECT * FROM inventory WHERE artist = ?;""", (artist_format,)).fetchall()

        if title in potential_conflicts: # If the title is there under this artist
            if format == potential_conflicts["format"]: # If the format is the same
                #We want to acknowledge this and send the user to the edit page to update the existing db entry's stock level
                return redirect(url_for('edit')) # <----- need to input the code variable somehow

        # Otherwise there's no clashing titles of the same format so we can continue as normal from here.
            
                # no problem we can add this to the db
        db.execute("""INSERT INTO inventory (title, artist, format, price, stock, genre, artwork)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", (title, artist_format, format, price, stock, genre, artwork))
        db.commit()
        outcome = "listing successfully added to the depth!"
        return render_template("new.html", form = form, outcome = outcome, title = "New release | the depth", caption = "List a new release")

    # If the form didn't validate upon submission, we just want to return the blank form.
    return render_template("new.html", form = form, title = "New release | the depth", caption = "List a new release")





# ________________________________________________________________________________________________________________________________________________________________
# EDIT RELEASE ??????????????????????????? Not working at all, but should be much the same /new route but with everything prepopulated with the information we have on file and the SQL should update rather than insert.

@app.route("/edit/<int:code>", methods = ["GET", "POST"])
@artist_login_required
def edit(code: int):
    """
    Allows an artist to edit stock or details of an existing release from the "view all releases" route
    """

    form = NewForm()

    outcome = ""

    db = get_db()

    edit_release = db.execute("""SELECT * FROM inventory WHERE code = ?;""", (code,)).fetchone()

    form.title.data = edit_release["title"]
    title = form.title.data
    form.format.data = edit_release["format"]
    format = form.format.data
    form.price.data = edit_release["price"]
    price = form.price.data
    form.stock.data = edit_release["stock"]
    stock = form.stock.data
    form.genre.data = edit_release["genre"]
    genre = form.genre.data

    if form.validate_on_submit(): # If the request is a POST request and that data is validated, then there is a catch it here
        # if it's a post, we want to send this info back to the db to update it
        for param in edit_release:
            value_to_update = form.param.data
            db.execute("""UPDATE inventory SET ? = ?;""", (param, value_to_update))
            db.commit()
        
        outcome = "release successfully updated!"

    
    # SQL to delete an entry: """DELETE FROM inventory WHERE code = _;"""
    
    return render_template("new.html", form = form, outcome = outcome, title = "Edit release | the depth", caption = "Edit")





# ________________________________________________________________________________________________________________________________________________________________
# VIEW RELEASES 

@app.route("/view_all", methods = ["GET", "POST"])
@artist_login_required
def view_all():
    """
    Allows an artist to view all of their current releases, with handy buttons to reach the pages for them to edit their listings and to view as fans would view them.
    """
    try:

        id = g.user

        db = get_db()

        display_all_releases = db.execute("""
        SELECT * FROM inventory
        WHERE artist =
        (SELECT artist_name FROM artists
        WHERE user_id = ?);
        """, (id, )).fetchall()



        artist = db.execute("""
        SELECT artist_name FROM artists
        WHERE user_id = ?;
        """, (id, )).fetchone()

        artist_str = ""
        for i in artist:
            artist_str += i



        return render_template("all_releases.html", display_all_releases = display_all_releases, artist = artist_str, title = "All your releases | the depth")

    except:

        return render_template("all_releases.html", title = "oops")





################################ helper functions called by other route functions ################################
# ________________________________________________________________________________________________________________________________________________________________
# ERROR

@app.errorhandler(404)
def page_not_found(error):
    """
    A means of presenting a specific page for a 404. We can make this better I think.
    """
    return render_template("404.html"), 404