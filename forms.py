from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DeleteForm(FlaskForm):
    id = IntegerField('ID Number of Puppy who was adoped: ')
    submit = SubmitField('Run to Your New Owner')

class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner: ')
    pup_id = IntegerField('Id of Pupp: ')
    submit = SubmitField('Add Owner')