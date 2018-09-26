from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email
from bson.objectid import ObjectId


#  wtform for Project Creation and Updation
class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired(), Length(min=2, max=30)])
    project_id = StringField('Project Id', validators=[DataRequired(), Length(min=1, max=10)])
    description = StringField('Description', validators=[DataRequired(), Length(min=5, max=30)])
    type = SelectField('Type', choices=[('Individual Project', 'Individual Project'), ('Team Project', 'Team Project'),
                                        ('Undecided', 'Undecided')], validators=[DataRequired()])
    submit = SubmitField('Submit')


#  wtform for User Creation and Updation
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email-id', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired()])
    place = StringField('Place', validators=[DataRequired()])
    projects = SelectMultipleField('Assign Projects', choices=[], coerce=ObjectId)
    submit = SubmitField('Submit')