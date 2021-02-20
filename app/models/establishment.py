from app import db
from . import ModelBase

class Establishment(ModelBase,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(100),nullable=True)
    about = db.Column(db.String(300),nullable=True)
    latitude = db.Column(db.BigInteger)
    longitude = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=True)