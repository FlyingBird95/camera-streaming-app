from flask import request, current_app
import jwt

from .blueprint import user_blueprint
from . import schema
from ... import errors, serialization
from ...models import USER_BY_ID


@user_blueprint.post("/authorize/<int:id>")
@serialization.serialize(schema.AuthorizationResponse)
def authorize(id):
    """Gets the user with the password and returns an authorization token."""
    payload = request.deserialize(schema.AuthorizeRequest)
    user = USER_BY_ID.get(id)
    if user is None:
        raise errors.NotFound("User is not found or incorrect password.")
    
    if payload["password"] != user.password:
        raise errors.NotFound("User is not found or incorrect password.")
    
    token = jwt.encode(
        payload={"user_id": user.id},
        key=current_app.config["SECRET_KEY"],
        algorithm=current_app.config["ALGORITHM"],
    )
    return {"user": user, "token": token}
