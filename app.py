# # # # # FLASK IMPORTS # # # # #
from flask import Flask, render_template, session, redirect, url_for, g, request
from flask_session import Session

# # # # # FORMS IMPORTS # # # # #
from forms import ContactForm, CordleForm, DungeonInitForm, BureaucracyInitForm, SudokuForm

# # # # # DATABASE IMPORTS # # # # # 
from database import get_db, close_db
from sqlite3 import IntegrityError

# # # # # PASSWORD SECURITY IMPORTS # # # # # 
from werkzeug.security import generate_password_hash, check_password_hash

# # # # # _____ IMPORTS # # # # #
from functools import wraps

# # # # # CONTACT FORM IMPORTS # # # # # 
import smtplib, ssl

# # # # # ASSORTED UTILITY IMPORTS # # # # # 
from random import randint, choice
import math
import datetime

# # # # # FLASK APP INITIALISATION # # # # #
app = Flask(__name__)

# # # # # DATABSE TEARDOWN # # # # #
app.teardown_appcontext(close_db)

# # # # # COOKIES & SESSION IMPORTS # # # # #

app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False # True would be persistent
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# # DO I EVEN NEED TO USE COOKIES FOR ANYTHING? Dark mode is being stored locally. Below details is just an example, I didn't write it for any specific use case.
# request.cookies.get("voted") == "yes":
# response.set_cookie("voted", "yes"; "dark-mode", "on"; id=cust123; expires=Sun 17-Jan-2042 19:14:07 GMT; "dark-mode", "on")





###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# OVERALL TO DO LIST:
# # # DO I HAVE THE RIGHT TERMS IN WHERE I'M CALLING A DB?
        # db.execute("""INSERT INTO gigs (band, gig_date)VALUES (?, ?)""", (band, gig_date))
        # db.commit()
# # #
# # #
# # #
# # #





###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# GLOBAL VARIABLES & GLOBAL FUNCTIONS
##########
# TO DO LIST
# - This is working, but I think I should be using Derek's pre-writen "g" code and not context_processor.

page_list = []

# @app.context_processor
# def context_processor():
#     date = datetime.datetime.now()
#     year = date.strftime("%Y")
    
#     directory()
#     return dict(year = year, page_list = page_list)

@app.before_request
def fill_g():
    date = datetime.datetime.now()
    g.year = date.strftime("%Y")




def directory():
    """
    A function to parse and collect all of the route names and add them to a list
    """

    # page_list = [
    #     "/contact",
    #     "/assorted",
    #     "/video",
    #     "/audio",
    #     "/threed",
    #     "/graphics",
    #     "/web",
    #     "/games",
    #     "/morse",
    #     "/javascript_projects",
    #     "/python_projects"
    # ]

    for rule in app.url_map.iter_rules():

        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):

            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if (url, rule.endpoint) not in page_list:
                page_list.append((url, rule.endpoint))

    return page_list



def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)



###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# HOME
##########
# TO DO LIST
# - 

@app.route("/", methods = ["GET", "POST"])
def index():
    """
    A home screen route.
    No requirement for any programming, as it is only calling the HTML page for the index.
    """
    try:
        return render_template("index.html", title = "Home")
    except:
        return render_template("index.html", title = "ERROR")











###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# SITE MAP
##########
# TO DO LIST
# - 

@app.route("/site_map")
def site_map():
    """
    A route that collects and displays a full list of every page available on the site.
    """
    try:

        return render_template("site_map.html", title = "Site Map")

    except:
        return render_template("site_map.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# ERROR
##########
# TO DO LIST
# - 

@app.errorhandler(403)
def page_not_found(error):
    return render_template("404.html", error_message = 404, title = "PAGE NOT FOUND")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error_message = 404, title = "PAGE NOT FOUND")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# CONTACT
##########
# TO DO LIST AT SOME STAGE
# - 

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    """
    A route for presenting the contact form.
    Also contains the programming for sending the email to my personal account through the SMTP protocol.
    Most principles for which are taken from here: https://realpython.com/python-send-email/#sending-a-plain-text-email
    However, my personal password and address have been saved with the password hash function.
    """
    form = ContactForm()

    try:
        
        message = ""

        if form.validate_on_submit():
            
            port = 465  # For SSL



            receiver_email = "donaghsugrue@gmail.com"
            password = "De@thGrippin23" # # # # # # # # # # CALL PASSWORD FROM DB W PASSWORD HASH # # # # # # # # # # 



            # Create a secure SSL context
            context = ssl.create_default_context()

            sender_name = form.name.data
            sender_email = form.email.data
            subject = form.subject.data
            body = form.message.data

            with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
                server.login(receiver_email, password) # My own info 
                server.sendmail(sender_name, sender_email, subject, body) # The info that is being sent through the form

            message = "Message sent! We will be back to your shortly."

        return render_template("contact.html", title = "Contact", form = form, message = message)
    except:
        return render_template("contact.html", title = "ERROR", form = form)












###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# ASSORTED
##########
# TO DO LIST
# - 

@app.route("/assorted", methods = ["GET", "POST"])
def assorted():
    """
    """
    try:
        return render_template("assorted.html", title = "Assorted")
    except:
        return render_template("assorted.html", title = "ERROR")











###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# VIDEO
##########
# TO DO LIST
# - Make a custom looking video player

@app.route("/video", methods = ["GET", "POST"])
def video():
    """
    """
    try:
        return render_template("video.html", title = "Video")
    except:
        return render_template("video.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# AUDIO
##########
# TO DO LIST
# - Make a custom looking audio player

@app.route("/audio", methods = ["GET", "POST"])
def audio():
    """
    """
    try:
        return render_template("audio.html", title = "Audio")
    except:
        return render_template("audio.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# 3D
##########
# TO DO LIST
# - 

@app.route("/3d", methods = ["GET", "POST"])
def threed():
    """
    """
    try:
        return render_template("3d.html", title = "3D Modelling")
    except:
        return render_template("3d.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# GRAPHICS
##########
# TO DO LIST
# - 

@app.route("/graphics", methods = ["GET", "POST"])
def graphics():
    """

    """
    try:
        db = get_db()
        graphics = db.execute("""SELECT * FROM graphics;""").fetchall() # Call all of the graphics projects in our db and send them to the jinja
        # graphics = db.execute("""SELECT * FROM graphics WHERE _____ = ?;""", (VARIABLE,)).fetchall() # Call all of the graphics projects in our db and send them to the jinja


        return render_template("graphics.html", title = "Graphics", graphics = graphics)
    except:
        return render_template("graphics.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# WEB
##########
# TO DO LIST
# - 

@app.route("/web", methods = ["GET", "POST"])
def web():
    """
    """
    try:
        db = get_db()
        sites = db.execute("""SELECT * FROM websites ORDER BY title DESC;""").fetchall() # Call all of the web development projects in our db and send them to the jinja

        return render_template("web.html", title = "Web", sites = sites)
    except:
        message = "We weren't able to collect the information ont he websites at this time. Please click here to contact us."
        return render_template("web.html", title = "ERROR", message = message)










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# GAMES
##########
# TO DO LIST
# - Could we use variables in the URL like this as cheat codes?
    # @app.route("/wine/<int:wine_id>")
    # def wine(wine_id):
# - 
# -

@app.route("/games", methods = ["GET", "POST"])
def games():
    """
    A homepage route for the various Javascript games hosted on the portfolio website.
    Each game will also have a route to where that specific game can be played.
    """
    try:

        # Collect the names of all the routes that start with "/games/" and put them in a list
        # Search the items of this list in the database
        # Cycle that in Jinja to display thumbnails for each game on the /games route

        return render_template("games.html", title = "Games")

    except:

        # If it reaches error, then the formula must be struggling to collect from the db.
        # If this is the case, call them from the global sitemap list and just return them as a list

        return render_template("games.html", title = "ERROR")










@app.route("/store_score", methods=["POST"])
def store_score():
    name = session["name"]
    score = int(request.form["score"])
    db = get_db()
    db.execute("""INSERT INTO leaderboard (player_name, score) VALUES (?, ?);""", (name, score))
    db.commit()
    return render_template("game.html", message = "SCORE SUCCESSFULLY ADDED TO LEADERBOARED", title = "GAME")

@app.route("/game", methods = ["GET", "POST"])
def game():
    """
    """
    try:
        message = ""
        player = session["name"]
        db = get_db()
        leaderboard = db.execute("""SELECT * FROM leaderboard ORDER BY score DESC;""").fetchmany(20) # Choose the top 5 best from the leaderboard to display
        return render_template("game.html", title = "DUNGEON CRAWLER 2000", player = player, leaderboard = leaderboard)
    except:
        message = "The game didn't load correctly. Please reload the page. If it still isn't working, please click here to contact us."
        return render_template("game.html", title = "ERROR", message = message)





# _______________________________________________________________________________________________________
# SNAKE

@app.route("/games/snake", methods = ["GET", "POST"])
def snake():
    """
    A route to present the Javascript game Snake.
    INSTRUCTIONS:
        -
        -
        -
    """
    try:
        return render_template("snake.html", title = "Snake")
    except:
        return render_template("snake.html", title = "ERROR")





# _______________________________________________________________________________________________________
# CORDLE

@app.route("/games/cordle", methods = ["GET", "POST"])
def cordle():
    """
    A route to present the Javascript game CORDLE.
    INSTRUCTIONS:
        - This is WORDLE but for Irish townlands comprised of 5 letters.
        - A new townland every 24hrs.
        - 
    """
    try:
        return render_template("cordle.html", title = "CORDLE")
    except:
        return render_template("cordle.html", title = "ERROR")


def Cordle(n):
    """
    Wordle, but you are searching for irish townlands that have 5 letters.
    """

    try:

        # Get all the possible answers from our txt file and create an empty list for them
        five_letter_file = open("five_letter_townlands.txt", "r")
        five_letter_townlands = []

        # Parse the file and extract the ones that are 5 letters (this is just additional clearance to prevent errors)
        for line in five_letter_file:
            if len(line) == 5:
                five_letter_townlands.append(line.lower())

        hurdleGuess = str(n) # cast to string, just to be sure
        hurdleGuess = hurdleGuess.lower() # for uniformity and avoiding ascii issues, we'll cast it all to lower case
        hurdleWord = str(session["HurdleWord"])

        if session["counter"] >= 6: # The user has made too many attempts so has lost
            return "YOU LOSE"

        elif hurdleGuess not in five_letter_words: # The user has guessed a word not in our library. This shouldn't be a guess, so just return an error.
            return "invalid word"

        elif hurdleGuess == hurdleWord: # The user has guessed correctly, they win!
            numberPreviousGuesses = str(session["counter"])
            session.clear() # clear the session to allow the user to start again at this point
            return f"YOU GUESSED CORRECTLY, {hurdleGuess} was correct and it only took you {numberPreviousGuesses} guesses!"

        else:
            previous_guesses.append(hurdleGuess)
            # score = scoring(hurdleWord, hurdleGuess) # run the scoring function
            counter += 1

            return "Nope, try again"

    except ValueError:
        return "oopsie daisy"            

        # if form.validate_on_submit(): # If the request is a POST request, catch it here
            # In response to a POST request, it checks and increments the number of guesses the user has made (in the session store)
            # if the number of guesses is not too many, it compares the user's guess (from the form) with the secret (from this user's session store) and sends the scores to the user.
            # The user gets no more than six guesses.
            # But if the user guesses a non-word, it doesn't count against her.

            #####################
            #####################
            #####################

            # If the Hurdle has been finished, we should clear the session and start again with a new secret word

        # else:
            # In response to a GET request, it chooses a secret five-letter word
            # it puts it into this user's session store
            # it also puts into the session store the number of guesses the user has made (zero!)
            # it sends a form to the user that allows the user to enter a guess.
            # return render_template("hurdle.html", form = form, title = "___") # Would reach here as a GET request

#__________________________________________________________________________________________________________________________________
# Listify


def listify():

    list_of_lists = []

    with open("five_letter_words.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)

    print(list_of_lists)








# _______________________________________________________________________________________________________
# DUNGEON CRAWLER 2000
##########
# TO DO LIST
# - 

@app.route("/games/dungeon_crawler_2000", methods = ["GET", "POST"])
def dungeon_crawler_2000():
    """
    A homepage route for the various Javascript games hosted on the portfolio.
    Each game will also have a route where that specific game can be played.
    """
    try:
        return render_template("games.html", title = "Dungeon Crawler 2000")
    except:
        return render_template("games.html", title = "ERROR")










# ______________________________________________________________________________________________________
# BEAURACRACY SIMULATOR
##########
# TO DO LIST
# - TRY USE THIS IN BUYREACRACY SIMULATOR TO MIMIC REALTIME
    # gig_date <= date.today():
    # datetime.now().strftime("%H:%M:%S %d-%m-%y")

@app.route("/games/beauracracy_simulator", methods = ["GET", "POST"])
def beauracracy_simulator():
    """
    A homepage route for the various Javascript games hosted on the portfolio.
    Each game will also have a route where that specific game can be played.
    """
    try:
        return render_template("beauracracy_simulator.html", title = "Beauracracy Simulator")
    except:
        return render_template("beauracracy_simulator.html", title = "ERROR")










###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# ASSORTED JAVASCRIPT PROJECTS
##########
# TO DO LIST
# - "Leave me a drawing" drawing app
# - Live stream platform for me to stream to my site
# - 

@app.route("/javascript", methods = ["GET", "POST"])
def javascript():
    """
    """
    try:
        javascript = "<script src='{{ url_for('static', filename='assorted_js_projects/libraries/p5.min.js') }}'</script> <script src='{{ url_for('static', filename='assorted_js_projects/libraries/p5.sound.min.js') }}'</script>"
        return render_template("javascript.html", title = "Javascript projects", javascript = javascript)
    except:
        return render_template("javascript.html", title = "ERROR")
# ______________________________________________________________________________________________________
# WEBCAM ASCII EFFECT
##########
# TO DO LIST
# - 

@app.route("/javascript/ascii", methods = ["GET", "POST"])
def ascii_video():
    """
    
    """
    try:

        javascript = "assorted_js_projects/sketch.js"

        return render_template("ascii.html", title = "ASCII Video", javascript = javascript)
    except:
        return render_template("ascii.html", title = "ERROR")



# ______________________________________________________________________________________________________
# WEBCAM DITHER EFFECT
##########
# TO DO LIST
# - 



# ______________________________________________________________________________________________________
# GUITAR TUNER
##########
# TO DO LIST
# - 













###############################################################################################################################################################################################################
# _____________________________________________________________________________________________________________________________________________________________________________________________________________
# ASSORTED PYTHON PROJECTS
##########
# TO DO LIST
# - 

python_list = [
    "twitter_bot()",
    "currency_converter()"
    ]

@app.route("/python", methods = ["GET", "POST"])
def python():
    """
    """
    try:
        return render_template("contact.html", title = "Python")
    except:
        return render_template("contact.html", title = "ERROR")

# ______________________________________________________________________________________________________
# TWITTER BOT
##########
# TO DO LIST
# - 

def twitter_bot():
    """
    """
    try:
        return
    except:
        return


# ______________________________________________________________________________________________________
# API CURRENCY CONVERTER
##########
# TO DO LIST
# - 

def currency_converter():
    """ForEx Trading for the layman with this nifty little function.
    Updates automatically through an API and to increase the list of currencies all you need do is update the URL variable."""

    try:
    # First of all get's the API endpoint data
        URL = "http://api.exchangeratesapi.io/v1/latest?access_key=d74db303c158223654168443bcbb8217&base=EUR&symbols=CNY,GBP,JPY,USD"

    # Uses the inbuilt requests module to GET the information from the API
        response = requests.get(URL)

    # Parse the API info to only the dictionary content
        parse_1 = str(response.content)[82:]
        parse_2 = parse_1[:-2:]

    # Eval this info to make a Dictionary of the currencies and their latest values.
    # The way I've done this should be scaleable, so if I introduce new currencies this eval method and the previous parse should be able to deal w it once the URL is changed.
        currency_dict = eval(parse_2)

    # # Currency Dictionary from previous version, commented out for reference.
        # currency_dict = {
                    
        #     "CNY": 7.7535,
        #     "GBP": 0.87538,
        #     "JPY": 132.3607,
        #     "USD": 1.1983
                
        # }

    # Render the basic form if using a GET method, send the dictionary to fill the radio buttons.
        if request.method == "GET":
            return render_template("currency_form.html", currency_dict = currency_dict)
        
        else:
    # If the euro field or the radio buttons are empty, send back an error message.
            if request.form["euro"] == "" or request.form["currency"] == "" :
                error_message = "ERROR: field's cannot be blank"
                return render_template("currency_form.html", error_message = error_message, currency_dict = currency_dict)

            else:
    # First we'll cast the euro amount to a float as we are rounding to 2 decimal places as it is a currency.
                euro_amount = round(float(request.form["euro"]), 2)

    # We'll then call what currency was seleted from the form, and search for it's index in the dictionary and save this to a new variable.
                form_call = request.form["currency"]
                currency = float(currency_dict[form_call])

    # The value we want to return is the currency exchange rate x by the euro amount rounded to 2 decimal places.
    # This is returned into a disabled text box.
                return_value = round(euro_amount * currency, 2)
                return render_template("currency_form.html", return_value = return_value, euro_amount = euro_amount, form_call = form_call, currency_dict = currency_dict)
    
    except Exception as e:
    # This should be a pretty unattainable exception. It's just to foolproof the code, and keep me amused.
        error_message = f"Ouch, whatever you did returned the following error: {str(e)} and it kind of hurt. Please don't do it again. :("
        return render_template("currency_form.html", error_message = error_message, currency_dict = currency_dict)


# ______________________________________________________________________________________________________
# AIRBNB / BOOKING SCRAPER
##########
# TO DO LIST
# - 

def aribnb_scraper():
    """
    """
    try:
        return
    except:
        return


# ______________________________________________________________________________________________________
# 3D ENGINE
##########
# TO DO LIST
# - 

def threed_engine():
    """
    Concepts taken from here: https://youtu.be/M_Hx0g5vFko
    """
    try:
        return
    except:
        return


# ______________________________________________________________________________________________________
# SUDOKU SOLVER
##########
# TO DO LIST
# - 

@app.route("/sudoku", methods=["GET", "POST"])
def SudokuSolver(sudo_dict: dict) -> str:
    """
    It's about that time of the week again.
    Donagh is trying to do his Sudoku puzzle and failing horrifically.
    So he turns to me AGAIN to complete the puzzle for him AGAIN.
    To do this, he'll have to input a sudoku puzzle that is too difficult for his feaible mind to complete as a dictionary.

    The keys for the dictionary should be integers numbered 0 - 8.
    The keys are equivalent to our rows.

    The value at each key should be a list of 9 values from left to right.
    The index of these values will be equivalenet to our column numbers 0 - 8.

    For the blank space that Donagh can't figure out, put any other character or symbol that isn't a digit 1 - 9.
    Preferably you should put an underscore / "_"
    """
    try:

        ########## TYPE ERROR ##########
        # Our script can only handle dictionaries in it's current form so I want an if to block anything that isn't a dictionary getting past.

        if type(sudo_dict) != dict:
            return """
Sorry chief, this script can only handle input in the form of a dictionary.
Maybe rewrite your input like the below dictionary and replace each _ with the numbers that have already been solved:
dict = {
    0   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    1   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    2   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    3   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    4   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    5   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    6   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    7   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    8   : ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
}
            """



        ########## CASTING ETC ##########
        for row in sudo_dict:
            # If the key isn't an int, we're screwed so I'll just let exceptions handle that.
            # Otherwise, I want to endeavour to cast things as much as I can.

            if type(sudo_dict[row]) != list:
                if type(sudo_dict[row]) == tuple:
                    sudo_dict[row] = list(sudo_dict[row])

                elif type(sudo_dict[row]) == str:
                    single_use_list = []
                    for i in sudo_dict[row]:
                        single_use_list.append(i)
                    sudo_dict[row] = single_use_list
                
                elif type(sudo_dict[row]) == int:
                    single_use_list = []
                    for i in str(sudo_dict[row]):
                        single_use_list.append(i)
                    sudo_dict[row] = single_use_list

                else:
                    return "Sorry, I wasn't able to understand your input. Please make sure it's a dictionary with keys as ints 0 - 8, and each value as a list with 9 entrys"

            # If the row was already a list, cool, but I want to check each cell in that list too and insure they're strings.
            temp_list = []
            for cell in sudo_dict[row]:
                temp_list.append(str(cell)) # cast it and add it
            sudo_dict[row] = temp_list
            # if this causes an exception, so be it.





        ########## SETTING UP THE WHILE LOOP ##########
        # Cool, now that we know the input is the correct type, we want to set up a while loop to figure out how many blanks we need to solve.

        ####################################################### THIS IS A GAMMY APPROACH, FIX THIS #######################################################
        # I'm just using this list to compare against
        placeholder_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ####################################################### THIS IS A GAMMY APPROACH, FIX THIS #######################################################

        to_solve = 0 # this loop calculates how many blank's or unknown cells need to be solved
        for row in sudo_dict:
            for cell in sudo_dict[row]:
                if cell not in placeholder_list: #### <------ connected to gammy bit
                    to_solve += 1

        counter = 0 # our while loop will continue until this is equal to the number of blanks to solve

        error_handler = 0 # and this variable is just to prevent for loops searching infinitely.

        # We want to keep our while loop alive as long as there are cells that need to be solved.
        while counter < to_solve:

            if error_handler > 1000: # basically, if the while loop runs more than a thousand times without solving any blanks, we can reasonably assume the puzzle is unsolvable
                error = "This puzzle wasn't able to be solved. Please double check the input, and maybe this error will help: \n The Sudoku Solver went through more than a thousand cycles without solving any blanks - so the input is likely incorrect or the puzzle is impossible."
                return error



        #####################################################################################################################
        #                                                                                                                   #
        #   I originally used the .index() function and it was doing a super annoying thing                                 #
        #   that took me hours to figure out that I want to share it                                                        #
        #           ["_", "9", "_", "_", "_", "7", "5", "2", "_"]                                                           #
        #   If i tried to find the index of [3] from this list by using .index(), it would return [0]                       #
        #               Every                           time.                                                               #
        #   I was going nuts trying to troubleshoot code I couldn't find a logical flaw with.                               #
        #   Took me hours to solve.         Literal hours.      HOURS!                              ....hours               #
        #   Anyway, This box is just my little private therapy session for myself                                           #
        #   (:                                                                                                              #
        #                                                                                                                   #
        #####################################################################################################################

        ########## SETTING UP THE REMAINDER OF OUR LOOP ##########
            for row in sudo_dict: # for every row in sudo_dict
                col_count = 0 # need to create a counter to deal with the issue of items in a list being indistinct from each other. Most specifically the .index() function when looking through a list w multiple "_"

                for cell in sudo_dict[row]: # check each cell
                    potential_numbers = [] # we'll use a blank list to populate w all the potential answers to this cell

        # if this cell has something in it already, we want to skip it
        # but if it isn't in the list IE if it's blank, then we'll continue w the main part of the function to solve it
                    if cell not in placeholder_list: # only examine cell if it doesn't have 1 - 9 in it ### <------ connected to gammy bit, 

        ########## ROWS ##########
        # Rows will all have the same key, so we want to check if the number we're looking at is in the key           
                        for number in range (1, 10): # starting from 1 going to 9
                            if str(number) not in sudo_dict[row]: # If the number as a string is in the list at the key, then the number is in the row so it's not a candidate. 
                                potential_numbers.append(str(number)) # Otherwise, it's a potential candidate for this cell, so add it to our single use list as a string.

        ########## COLUMNS ##########
        # So after checking in the row, there can't be anything in potential_numbers that won't be the number so we won't be adding anything else.
        # But we can't leave it there - if the number we're looking at isn't possible based on the column (IE is in the column) but is already in potential numbers then we need to remove it.
        # Columns will all have the same index, so we want to check if the number we're looking at has a twin in another row with the same index
                        col_content = [] # empty list to store the contents of the column
                        for number in range(1, 10): # starting from 1 going to 9
                            for row_cycle in sudo_dict: # doing a new for loop in sudo_dict to cycle through the rows  
                                col_content.append(str(sudo_dict[row_cycle][col_count])) # and add this to a single use list to show the content of a column
                        for item in col_content:    
                            if item in col_content and item in potential_numbers: # if the was in the column and is in potential_numbers, then we need to remove it as a potential number
                                potential_numbers.remove(item)

        ########## BOXES ##########
        # We'll make a list for this for loop and call it "box content"
        # We have 9 boxes with coordinates arranged as such:
            # 1, 1      1, 2        1, 3
            # 2, 1      2, 2        2, 3
            # 3, 1      3, 2        3, 3
        # If we take the index of the cell we're on, add one, divide by 3 and round up then we'll know which column box we're in.
        # IE if we're in cell [4] + 1 is 5, divide by 3 rounded up is 2 so we're in the middle column of boxes
        # If we do the same with the key's then we'll know which row's belong in box_content
        # We'll cycle through every cell and add shared coordinates to box_content
                        box_content = []
                        box_horiz = math.ceil((col_count + 1) / 3) # Might be convoluted, but I want to check whether our cell is in box 1, 2 or 3 from left to right
                        box_vert = math.ceil((row + 1) / 3) # Might be convoluted, but I want to check whether our cell is in box 1, 2 or 3 from top to bottom 

        # we need to cycle through every cell now to find the other numbers in the box
                        for row_cycle in sudo_dict: # for each row
                            for cell_cycle in range(1, 10): # and for each cell
                                if math.ceil((row_cycle + 1) / 3) == box_vert and math.ceil(cell_cycle / 3) == box_horiz: # if the cell coordinates are in the same box as the number we're investigating                                     
                                    box_content.append(str(sudo_dict[row_cycle][cell_cycle - 1]))

                        for item in box_content: # going through each cell in our box
                            if item in box_content and item in potential_numbers: # if the number is in the box and was a potential number, we want to remove it's candidacy.
                                potential_numbers.remove(item)
                            # In the same way as above, there is no situation where a number isn't already present in potential_numbers that would be the right candidate so we don't need to add more numbers

        ########## AMEND OR REPEAT ##########
                        if len(potential_numbers) == 1: # if we've gone through this process and there's only one potential candidate for this cell
                            sudo_dict[row][col_count] = potential_numbers[0] # then we want to amend that entry
                            counter += 1 # and we want to reduce the number of counter by one as we're one closer to completing things
                            error_handler = 0 # and reset error_handler to 0

                    #############################################################
                    #                                                           #
                    #       I made a dumb little terminal loading bar           #
                    #       that shows the progress of the function.            #
                    #       Sometimes it could take a few seconds,              #
                    #       And tbh from the day we first printed to terminal   #
                    #       I've want to do exactly this.                       #
                    #                                                           #
                    #         print(loading_bar(counter, to_solve))             #
                    #                                                           #
                    #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^            #
                    #       Uncomment the above line and run again              #
                    #       if you want to see what I'm talking about. (:       #
                    #                                                           #
                    #############################################################
                            
        # if the len(potential_numbers) isn't 1, then we don't have a viable candidate for this cell.                
                        col_count += 1 # So we'll move to the next column and check their cells
                        error_handler += 1 # and increase our error handler so that we know we've done a pass through of it without solving a cell
        # We will inevitably come back to this cell on another run because the while loop will start the for loops again
                        
        ########## PROCESS A CELL ALREADY HAVING A NUMBER IN IT ##########                   
                    else: # Means that there's already a number at that entry
                        col_count += 1 # so just move to the next column

        ########## RETURN AS STRING ##########
        # Should only hit this point once there are 0 cells left to solve
        # I want to ultimately return the answer to the user as a string.
        return_str = ""

        # I'm going to use while loops as I'm going to do slightly different things depending on where in the loop it is
        row_count = 0

        while row_count < 9:
            col_count = 0

        # I want to have a line atop the box first so if we haven't had any other rows, we're putting a line
            if row_count == 0:
                return_str += "_______________________________\n"

            while col_count < 9:

        # If this is the first entry in a box, or if there have been 3 entries in a box, we want to have a | to divide the box
                if col_count == 0 or col_count % 3 == 0:
                    return_str += "|"
                return_str += " "
                return_str += sudo_dict[row_count][col_count]
                return_str += " "

                col_count += 1

        # At the end of a row, add a divider and move to the next line
            return_str += "|\n"

        # Every 3 rows, we want to add another line to divide the boxes horizontally
            if (row_count + 1) % 3 == 0:
                return_str += "_______________________________\n"

            row_count += 1

        # Finally, return the string we've made
        return return_str

        ########## EXCEPTION HANDLING ##########
    except Exception as e:
        error = "This puzzle wasn't able to be solved. Please double check the input, and maybe this error will help: \n"
        error += str(e)
        return error





































