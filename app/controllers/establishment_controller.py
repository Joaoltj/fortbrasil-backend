from flask import Blueprint,request
from app.models.establishment_model import Establishment
from app.services import establishment_service
from app.schemas.establishment_schema import EstablishmentSchema
from app import utils

establishment_controller = Blueprint('establishment',__name__)
schema = EstablishmentSchema()

@establishment_controller.route('',methods=['GET'])
def get_establishments():
    pass

@establishment_controller.route('/<int:id>',methods=['GET'])
def get_by_id_establishment(id):
    pass

@establishment_controller.route('',methods=['POST'])
def post_establishment():
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return utils.response_bad_request(errors)
    establishment = Establishment(**data)
    establishment, error = establishment_service.save_establishment(establishment)
    if error:
        return utils.response_server_error(error)
    return utils.response_created(schema.dump(establishment))

@establishment_controller.route('/<int:id>',methods=['PUT'])
def put_establishment(id):
    pass

@establishment_controller.route('/<int:id>',methods=['DELETE'])
def delete_establishment(id):
    pass
