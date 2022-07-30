from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeCreationForm(FlaskForm):
    poke_name = StringField('Pokemon', validators=[DataRequired()])
    submit = SubmitField()