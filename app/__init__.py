from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flask.cli import with_appcontext
from app.config import Config
import click



db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    CORS(app)

    from app.models.establishment_model import Establishment
    from app.models.user_model import User

    from app.controllers.establishment_controller import establishment_controller
    from app.controllers.user_controller import user_controller

    app.register_blueprint(establishment_controller,url_prefix='/establishments')
    app.register_blueprint(user_controller,url_prefix='/user')
    return app



app = create_app()
print(app.url_map)

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    with app.app_context():
        db.create_all()

app.cli.add_command(create_tables)
