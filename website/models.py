#defining DB tables

from . import db #imports db object from . (current package: init.py/website)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #associating notes with each user (relationships/foreign key)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #many-one relationship with notes->user
    

class User(db.Model, UserMixin):
    #define all columns to be stored
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #adds note ID into User DB to let user see all notes
    notes = db.relationship('Note')

