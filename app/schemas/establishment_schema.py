from app import ma
from marshmallow import fields,validate


class EstablishmentSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(0, 100),allow_none=False)
    description = fields.Str(required=False, validate=validate.Length(0, 100),allow_none=True)
    about = fields.Str(required=False, validate=validate.Length(0, 300),allow_none=True)
    latitude = fields.Int(required=True,allow_none=False)
    longitude = fields.Int(required=True,allow_none=False)


