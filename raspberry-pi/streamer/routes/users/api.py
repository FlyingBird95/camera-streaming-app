from functools import wraps

from flask import request

from ... import errors


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        if not request.user:
            raise errors.Unauthorized("Authentication Token is missing or incorrect")

        return f(*args, **kwargs)

    return decorated
