from app import ma
from marshmallow import fields,validate


class UserRegisterSchema(ma.Schema):
    name = fields.Str(required=True, validate=validate.Length(0, 100),allow_none=False)
    email = fields.Email(required=True, validate=validate.Length(0, 100),allow_none=False)
    password = fields.Str(required=True, validate=validate.Length(8, 50),allow_none=False)



class UserLoginSchema(ma.Schema):
    email = fields.Email(required=True, validate=validate.Length(0, 100),allow_none=False)
    password = fields.Str(required=True, validate=validate.Length(8, 50),allow_none=False)



