from flask import Blueprint

user_blueprint = Blueprint("user", __name__, url_prefix="/users")

from . import authorize, get, post  # noqa