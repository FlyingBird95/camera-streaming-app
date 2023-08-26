from typing import Optional

from flask import current_app, Request as RequestBase, request
import jwt
from jwt import DecodeError
from marshmallow import ValidationError

from .models import User, USER_BY_ID
from . import errors


class Request(RequestBase):
    
    @staticmethod
    def deserialize(schema_class):
        schema = schema_class()
        try:
            return schema.load(request.json)
        except ValidationError as e:
            raise errors.BadRequest(description=e.messages_dict)
    
    @property
    def user(self) -> Optional[User]:
        token = self.headers.get("Authorization")
        if not token:
            return None
        
        try:
            data = jwt.decode(
                jwt=token,
                key=current_app.config["SECRET_KEY"],
                algorithms=[current_app.config["ALGORITHM"]],
            )
        except DecodeError:
            return None
        
        return USER_BY_ID.get(data["user_id"])
