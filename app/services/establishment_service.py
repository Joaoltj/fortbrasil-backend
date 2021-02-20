from app import db
from datetime import datetime
from app.models.establishment_model import Establishment

def save_establishment(establishment):
    try:
        establishment.created_at = datetime.now()
        db.session.add(establishment)
        db.session.commit()
        return establishment,False
    except Exception as e:
        return False, e.__str__()



def get_establishment(id):
    try:
        establishment = Establishment.query.filter_by(id=id).first()
        return establishment,False
    except Exception as e:
        return False, e.__str__()
