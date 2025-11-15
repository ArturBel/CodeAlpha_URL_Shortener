from flask import Flask
from api.config import Config
from api.extensions import db, migrate
from api.routes import shorten_bp
from api.models import Urls


def create_app():
    # creating and configuring app instance
    app = Flask(__name__)
    app.config.from_object(Config)

    # initializing extensions
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    # registering blueprints
    app.register_blueprint(shorten_bp)

    # setting up health endpoint
    @app.route('/health')
    def health():
        return "API works correctly"

    return app