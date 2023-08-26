from flask import Flask, jsonify

from .routes.main.blueprint import main_blueprint
from .routes.video.blueprint import video_blueprint
from .routes.users.blueprint import user_blueprint

from .config import config_by_name
from .request import Request
from . import errors


def create_app(config_name="production"):
    app = Flask(__name__)
    app.request_class = Request
    
    config_obj = config_by_name[config_name]()
    app.config.from_object(config_obj)
    
    # Registering blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(video_blueprint)
    app.register_blueprint(user_blueprint)
    
    @app.errorhandler(errors.ApiError)
    def handle_exception(error: errors.ApiError):
        return jsonify(
            {
                "message": error.message,
                "description": error.description,
            }
        ), error.status_code

    return app