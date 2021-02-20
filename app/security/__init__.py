from functools import wraps
import jwt
from time import time
from app.models.user_model import User
import bcrypt

def get_app():
    from app import app
    return app

def encrypt_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(str.encode(password), salt)
    return hashed.decode('UTF-8')

def check_password(password,hashed):
    if bcrypt.checkpw(password.encode('utf-8'),hashed.encode('utf-8')):
        return True
    else:
        return False

def generate_token(data):
    print(get_app().config.get('TIME_EXPIRATION'))
    data['expiration'] = int(time()*1000) + get_app().config.get('TIME_EXPIRATION')
    return enconde(data)

def enconde(data):
    encoded = jwt.encode(data, get_app().config.get('SECRET_KEY'), algorithm='HS256')
    return encoded

def decode(enconde):
    decode = jwt.decode(enconde, get_app().config.get('SECRET_KEY'), algorithm='HS256')
    return decode

def validate_token(data):
    usuario = User.query.filter_by(id=data['id']).first()
    if(data['expiration'] > int(time()*1000) or not usuario):
        return False
    return True

def security_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from flask import request
        token = request.headers.get('Authorization')
        error = {'error':'invalid token'},401
        if not token:
            return error
        try:
            token_decoded = decode(token)
            if not validate_token(token_decoded):
                return error
        except:
            return error

        return func(*args, **kwargs)

    return wrapper

