from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask.cli import with_appcontext
from app.config import Config
import click



db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    return app



app = create_app()
print(app.url_map)

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    with app.app_context():
        db.create_all()

app.cli.add_command(create_tables)
