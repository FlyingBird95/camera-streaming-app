import marshmallow


class User(marshmallow.Schema):
    """User response schema."""
    
    id = marshmallow.fields.Integer(required=True)
    
    name = marshmallow.fields.String(required=True)


class CreateUser(marshmallow.Schema):
    """Create user deserialization schema."""

    name = marshmallow.fields.String(required=True)
    
    password = marshmallow.fields.String(required=True)


class AuthorizeRequest(marshmallow.Schema):
    """Authorize request schema for deserialization."""
    
    password = marshmallow.fields.String(required=True)


class AuthorizationResponse(marshmallow.Schema):
    """Authorization response schema."""
    token = marshmallow.fields.String(required=True)
    
    user = marshmallow.fields.Nested(User())
