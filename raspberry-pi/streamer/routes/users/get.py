from flask import request
from .api import token_required
from .blueprint import user_blueprint
from . import schema
from ... import errors, serialization


@user_blueprint.get("/<int:id>")
@token_required
@serialization.serialize(schema.User)
def get(id):
    if not request.user or request.user.id != id:
        raise errors.NotFound("User is not found")
    
    return request.user
