from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    last_name = StringField('Please enter your last name?', validators=[DataRequired()])
    search = SubmitField('SEARCH')
