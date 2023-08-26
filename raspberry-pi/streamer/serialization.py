from http import HTTPStatus
import functools
from typing import Any, Dict

import attr

from flask import Response, make_response


def serialize(schema_class):
    """Serialize the API call result with the schema.

    :param schema_class: Schema class to use for the serialization.

    :return: Decorator that applies the serialization to a function.
    """

    def wrapper(func):

        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, Response):
                return result
            
            schema = schema_class()
            response_params = result if isinstance(result, ResponseParams) else ResponseParams(data=result)
            data = schema.dump(response_params.data)
            response = make_response(data, response_params.status_code)
            response.headers.update(response_params.headers)
            return response

        return func_wrapper

    return wrapper


@attr.s(kw_only=True)
class ResponseParams:
    """Additional response parameters."""

    data: Any = attr.ib()
    """Data to be serialized. Can either be an object, or a dictionary."""

    status_code: HTTPStatus = attr.ib(default=HTTPStatus.OK)
    """Status code if not a 200 (HTTPStatus.OK)."""

    headers: Dict[str, Any] = attr.ib(default=attr.Factory(dict))
    """Additional response headers."""

