from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddUserForm(FlaskForm):
    name=StringField('Username',validators=[DataRequired()])
    submit=SubmitField('Submit')

class DeleteTaskForm(FlaskForm):
    submit=SubmitField('Delete')