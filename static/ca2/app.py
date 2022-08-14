@app.route("/", methods = ["GET", "POST"])
def index():
    """
    A home screen route. Here we collect the users initials and store it in the session. We will save this with the score into the DB later.
    """
    try:
        form = InitialForm()

        if form.validate_on_submit(): # If the form validates, we want to save the info into the session and redirect to the game
            
            session["name"] = form.initial.data

            return redirect(url_for("game"))

        return render_template("index.html", title = "HOME | DUNGEON CRAWLER 2000", form = form) # If the form didn't validate, we want them to be on the home page

    except:
        return render_template("index.html", title = "ERROR")



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



@app.route("/store_score", methods=["POST"])
def store_score():
    
    name = session["name"]
    score = int(request.form["score"])
    db = get_db()
    db.execute("""INSERT INTO leaderboard (player_name, score) VALUES (?, ?);""", (name, score))
    db.commit()
    return render_template("game.html", message = "SCORE SUCCESSFULLY ADDED TO LEADERBOARED", title = "GAME")