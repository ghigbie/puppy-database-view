from myproject import db
import os

#from forms import AddForm, DeleteForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECREK_KEY'] == 'youwillneverguessme'


###SQL DATABASE SECTION #######
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#####MODELS######
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
 
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"