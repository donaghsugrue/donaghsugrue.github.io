from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, SelectField, StringField, TextAreaField, DecimalField, PasswordField # , FileField, 
from wtforms.validators import InputRequired, EqualTo #, NumberRange
#### Is there a way to use NumberRange to get the amount of stock that we have and use that as the max in NumberRange?



################################ general site stuff ################################ 
# ______________________________________________________________________________________________________________________________
class AddToCart(FlaskForm):

    quantity = IntegerField(
        "Stock:",
        validators = [InputRequired()],
        default = 1
        )

    submit = SubmitField(
        "Submit"
        )


# format = SelectField(
    #     "Format:",
    #     choices = []
    # )

#______________________________________________________________________________________________________________________________
class LibraryForm(FlaskForm):

    artist = SelectField("Artist:", choices = [""], validators = [InputRequired()])

    submit = SubmitField(
        "Submit"
        )

#______________________________________________________________________________________________________________________________

class ContactForm(FlaskForm):

    name = StringField(
        "Name:", validators = [InputRequired()]
    )

    subject = StringField(
        "Subject:", validators = [InputRequired()]
    )

    emailAddress = StringField(
        "Email:", validators = [InputRequired()]
    )

    message = TextAreaField(
        "Message:", validators = [InputRequired()]
    )

    submit = SubmitField(
        "Submit"
        )










################################ fan user specific ################################ 
# ______________________________________________________________________________________________________________________________
class FanLoginForm(FlaskForm):

    user_id = StringField("User id:", validators = [InputRequired()])

    password = PasswordField("Password:", validators = [InputRequired()])

    submit = SubmitField("Submit")

# ______________________________________________________________________________________________________________________________
class FanRegistrationForm(FlaskForm):

    user_id = StringField("User id:", validators = [InputRequired()])

    password = PasswordField("Password:", validators = [InputRequired()])

    password2 = PasswordField("Confirm Password:", validators = [InputRequired(), EqualTo("password")])

    submit = SubmitField("Submit")










################################ artist user specific ################################ 
#______________________________________________________________________________________________________________________________
class ArtistLoginForm(FlaskForm):

    user_id = StringField("User id:", validators = [InputRequired()])

    password = PasswordField("Password:", validators = [InputRequired()])

    submit = SubmitField("Submit")

#______________________________________________________________________________________________________________________________
class ArtistRegistrationForm(FlaskForm):

    artist_name = StringField("Artist name:", validators = [InputRequired()])

    user_id = StringField("User id:", validators = [InputRequired()])

    password = PasswordField("Password:", validators = [InputRequired()])

    password2 = PasswordField("Confirm Password:", validators = [InputRequired(), EqualTo("password")])

    submit = SubmitField("Submit")

#______________________________________________________________________________________________________________________________
class NewForm(FlaskForm):

    # code - needs to be auto generated based on how many releases have been submitted. Put AUTOINCREMENT in sql schema I think.

    title = StringField(
        "Title:",
        validators = [InputRequired()])

    # artist - This should come from the session as the Artist needs to be logged in, rather than be in the form.

    format = SelectField(
        "Format:",
        choices = ["Vinyl", "Tape", "CD", "USB", "Other"],
        validators = [InputRequired()]
        )

    price = DecimalField(
        "Price:",
        validators = [InputRequired()],
        default = 10.00
        )

    stock = IntegerField(
        "Stock:",
        validators = [InputRequired()]
        )

    genre  = StringField(
        "Genre:",
        validators = [InputRequired()]
        )

    # artwork = FileField()
    # Need to specify size, need to specify jpg, need to rename the file, need to place it into static

    submit = SubmitField(
        "Submit"
        )