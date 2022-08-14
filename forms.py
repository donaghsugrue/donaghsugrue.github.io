from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange



#______________________________________________________________________________________________________________________________
class ContactForm(FlaskForm):
    """
    Flask Form for the email contact form.
    App.py handles the message being sent via SMTP.
    """
    name = StringField(
        "Name:",
        validators = [
            InputRequired()
        ]
    )
    subject = StringField(
        "Subject:",
        validators = [
            InputRequired()
        ]
    )
    email = StringField(
        "Email address:",
        validators = [
            InputRequired()
        ]
    )
    message = TextAreaField(
        "Message:",
        validators = [
            InputRequired()
        ],
        default = "Put your message here"
    )

    submit = SubmitField()



#______________________________________________________________________________________________________________________________
class CordleForm(FlaskForm):
    """
    Form to take the 5 letter guess for CORDLE, an Irish Townland themed port of the hit web game WORDLE.
    """
    letter1 = StringField(
        validators = [
            InputRequired(),
            Length(min = 1, max = 1)
        ]
    )
    letter2 = StringField(
        validators = [
            InputRequired(),
            Length(min = 1, max = 1)
        ]
    )
    letter3 = StringField(
        validators = [
            InputRequired(),
            Length(min = 1, max = 1)
        ]
    )
    letter4 = StringField(
        validators = [
            InputRequired(),
            Length(min = 1, max = 1)
        ]
    )
    letter5 = StringField(
        validators = [
            InputRequired(),
            Length(min = 1, max = 1)
        ]
    )

    submit = SubmitField()



#______________________________________________________________________________________________________________________________
class DungeonInitForm(FlaskForm):

    initial = StringField(
        "PLEASE ENTER YOUR INITIALS:",
        validators = [
            InputRequired(),
            Length(min = 3, max = 3)]
    )
    submit = SubmitField(
        "CLICK HERE TO PLAY"
    )



#______________________________________________________________________________________________________________________________
class BureaucracyInitForm(FlaskForm):

    initial = StringField(
        "PLEASE ENTER YOUR INITIALS:",
        validators = [
            InputRequired(),
            Length(min = 3, max = 3)]
    )
    submit = SubmitField(
        "CLICK HERE TO PLAY"
    )



#______________________________________________________________________________________________________________________________
class SudokuForm(FlaskForm):
    """
    A flask form to take user input that can be applied and parsed with the sudoku function in app.py

    This is the logic of the form, and how it will be presented and deciphered from user to function:

    a1   a2   a3  |  a4   a5   a6  |  a7   a8   a9
    b1   b2   b3  |  b4   b5   b6  |  b7   b8   b9
    c1   c2   c3  |  c4   c5   c6  |  c7   c8   c9
    --------------+----------------+---------------
    d1   d2   d3  |  d4   d5   d6  |  d7   d8   d9
    e1   e2   e3  |  e4   e5   e6  |  e7   e8   e9
    f1   f2   f3  |  f4   f5   f6  |  f7   f8   f9
    --------------+----------------+---------------
    g1   g2   g3  |  g4   g5   g6  |  g7   g8   g9
    h1   h2   h3  |  h4   h5   h6  |  h7   h8   h9
    i1   i2   i3  |  i4   i5   i6  |  i7   i8   i9

    """

    a1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    a9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    b1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    b9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    c1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    c9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )


    
    d1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    d9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )


    
    e1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    e9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    f1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    f9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    g1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    g9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    h1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    h9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )


    
    i1 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i2 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i3 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i4 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i5 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i6 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i7 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i8 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )
    i9 = IntegerField(
        default = 0,
        validators = [
            NumberRange(min=0, max=9, message="Numbers must be between 1 and 9. If you don't know what value belongs in a cell, leave it at 0.")
        ]
    )



    submit = SubmitField()