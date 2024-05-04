from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, Optional, URL, Length

class AddPetForm(FlaskForm):
    """Form for adding pets to pet adoption database."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", validators=[InputRequired()], choices=[("cat", "cat"),("dog", "dog"),("rabbit", "rabbit")])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30"), Optional()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    
class EditPetForm(FlaskForm):
    """Form to a edit a pet on pet adoption database."""
    name = StringField("Pet Name", validators=[Optional()])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available? ")