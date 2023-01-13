from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
import click

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    
    # import models for Alembic Setup
    from app.models.customer import Customer
    from app.models.video import Video
    from app.models.rental import Rental

    # Setup DB
    db.init_app(app)
    migrate.init_app(app, db)

    #Register Blueprints Here
    from .routes.rental_routes import rentals_bp
    from .routes.video_routes import videos_bp
    from .routes.customer_routes import customers_bp
    app.register_blueprint(videos_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(rentals_bp)

    click.echo('Welcome to my store')


    @app.cli.command('hello')
    @click.option('--name', default='World')
    def hello_command(name):
        click.echo(f'Hello, {name}!')

    def test_hello():
        runner = app.test_cli_runner()

        # invoke the command directly
        result = runner.invoke(hello_command, ['--name', 'Flask'])
        assert 'Hello, Flask' in result.output

        # or by name
        result = runner.invoke(args=['hello'])
        assert 'World' in result.output

    return app