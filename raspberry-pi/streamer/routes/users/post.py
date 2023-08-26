from http import HTTPStatus

from flask import request


from .blueprint import user_blueprint
from . import schema
from ... import serialization
from ...models import User


@user_blueprint.post("")
@serialization.serialize(schema.User)
def post():
    """Create a new user in the system."""
    
    payload = request.deserialize(schema.CreateUser)
    user = User.create(name=payload["name"], password=payload["password"])
    return serialization.ResponseParams(data=user, status_code=HTTPStatus.CREATED)
