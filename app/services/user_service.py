from app import db
from datetime import datetime
from app.models.user_model import User
from app.security import encrypt_password,check_password

def validate_password(password,hash):
    try:
        return check_password(password,hash)
    except:
        return False

def get_user_by_email(email) -> User:
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        return None
    except:
        return None

def save_user(user):
    try:
        user.password = encrypt_password(user.password)
        user.created_at = datetime.now()
        db.session.add(user)
        db.session.commit()
        return user, False
    except Exception as e:
        return False, e.__str__()
