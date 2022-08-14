from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route("/xchange", methods=["GET", "POST"])
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
        error_message = "Ouch, whatever you did returned the following error: " + "\n" + str(e) + "\n" + " and it kind of hurt. Please don't do it again. :("
        return render_template("currency_form.html", error_message = error_message, currency_dict = currency_dict)