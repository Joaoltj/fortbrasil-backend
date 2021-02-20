from app import db
from datetime import datetime

def save_establishment(establishment):
    try:
        establishment.created_at = datetime.now()
        db.session.add(establishment)
        db.session.commit()
        return establishment,False
    except Exception as e:
        return False, e.__str__()