from flask import Blueprint,request
from app.models.user_model import User
from app.schemas.user_schema import UserRegisterSchema, UserLoginSchema, UserInfoSchema
from app.services import user_service
from app import utils
from app.security import generate_token, security_token, get_token_data


register_schema = UserRegisterSchema()
login_schema = UserLoginSchema()
info_schema = UserInfoSchema()

user_controller = Blueprint('user',__name__)

@user_controller.route('/login',methods=['POST'])
def user_login():
    data = request.get_json()
    errors = login_schema.validate(data)
    if errors:
        return utils.response_bad_request(errors)
    user = user_service.get_user_by_email(data.get('email',''))

    if not user:
        return utils.response_not_found('Usuário não encontrado.')

    valid_password = user_service.validate_password(data.get('password',''),user.password)
    if not valid_password:
        return utils.response_bad_request('E-mail e/ou senha inválidos')

    token = generate_token({'id':user.id})

    return utils.response_ok(token)


@user_controller.route('/register',methods=['POST'])
def user_register():
    data = request.get_json()
    errors = register_schema.validate(data)

    if errors:
        return utils.response_bad_request(errors)

    if user_service.get_user_by_email(data.get('email','')):
        return utils.response_bad_request('E-mail já possui cadastro.')

    user = User(**data)
    user,error = user_service.save_user(user)

    if error:
        return utils.response_server_error(error)

    return utils.response_created('Usuário criado com sucesso.')


@user_controller.route('/info',methods=['GET'])
@security_token
def user_info():
    data = get_token_data()
    if not data:
        return utils.response_bad_request('Erro desconhecido.')

    user,error = user_service.get_user(data.get('id',0))

    if error:
        return utils.response_bad_request(error)

    return utils.response_ok(info_schema.dump(user))


