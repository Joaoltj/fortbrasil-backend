from app import db
from . import ModelBase

class User(ModelBase,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
