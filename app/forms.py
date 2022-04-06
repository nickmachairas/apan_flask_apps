from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    username = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')
