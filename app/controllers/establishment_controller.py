from flask import Blueprint, request
from app.models.establishment_model import Establishment
from app.services import establishment_service
from app.schemas.establishment_schema import EstablishmentSchema
from app import utils
from app.security import security_token

establishment_controller = Blueprint('establishment',__name__)
schema = EstablishmentSchema()

@establishment_controller.route('',methods=['GET'])
@security_token
def get_establishments():
    establishments, error = establishment_service.get_establishments()

    if error:
        return utils.response_bad_request(error)

    return utils.response_ok(EstablishmentSchema(many=True).dump(establishments))


@establishment_controller.route('/<int:id>',methods=['GET'])
@security_token
def get_by_id_establishment(id):
    establishment,error = establishment_service.get_establishment(id)

    if error:
        return utils.response_bad_request(error)

    if establishment is None:
        return utils.response_not_found('Estabelecimento não encontrado.')

    return utils.response_ok(schema.dump(establishment))




@establishment_controller.route('',methods=['POST'])
@security_token
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
@security_token
def put_establishment(id):
    establishment,error = establishment_service.get_establishment(id)

    if error:
        return utils.response_bad_request(error)
    elif establishment is None:
        return utils.response_not_found('Estabelecimento não encontrado.')

    data = request.get_json()
    errors = schema.validate(data)

    if errors:
        return utils.response_bad_request(errors)

    establishment.update(data,['id'])
    establishment,error = establishment_service.save_establishment(establishment)

    if error:
        return utils.response_bad_request(error)
    return utils.response_ok(schema.dump(establishment))



@establishment_controller.route('/<int:id>',methods=['DELETE'])
@security_token
def delete_establishment(id):
    establishment, error = establishment_service.get_establishment(id)

    if error:
        return utils.response_bad_request(error)
    elif establishment is None:
        return utils.response_not_found('Estabelecimento não encontrado.')

    success,error = establishment_service.delete_establishment(establishment)

    if error:
        return utils.response_bad_request(error)

    return utils.response_ok('Estabelecimento excluído com sucesso.')