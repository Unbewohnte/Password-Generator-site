from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,RadioField,IntegerField,BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

class PasswordGenerationForm(FlaskForm):
    length = IntegerField('Length (1-100(Numbers only))', validators = [DataRequired(),NumberRange(min=1,max=100)],default=10)
    how_many_passwords = IntegerField('How many passwords (1-20)',validators=[DataRequired(),NumberRange(min=1,max=20)],default=1)
    Upper_register_field = BooleanField("Upper register")
    Digits_field = BooleanField("Digits")
    Punctuation_field = BooleanField("Punctuation")
    submit = SubmitField('Generate !')
    valid = False
