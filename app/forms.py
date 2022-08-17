from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    last_name = StringField('Please, enter your work e-mail?', validators=[DataRequired()])
    search = SubmitField('SEARCH')
