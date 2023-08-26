from http import HTTPStatus


class ApiError(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Internal server error"
    
    def __init__(self, description):
        self.description = description


class BadRequest(ApiError):
    status_code = HTTPStatus.BAD_REQUEST
    

class NotFound(ApiError):
    status_code = HTTPStatus.NOT_FOUND


class Unauthorized(ApiError):
    status_code = HTTPStatus.UNAUTHORIZED