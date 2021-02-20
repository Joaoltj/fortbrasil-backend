from flask import Blueprint
from app.models.user_model import User

user_controller = Blueprint('user',__name__)

@user_controller.route('/login',methods=['POST'])
def user_login():
    pass

@user_controller.route('/register',methods=['POST'])
def user_register():
    pass


@user_controller.route('/info',methods=['GET'])
def user_info():
    pass
