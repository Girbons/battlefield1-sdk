
class InvalidAPIKey(Exception):
    """
    Invalid API Key
    """


class Redirection(Exception):
    """
    Redirection
    """


class BadRequest(Exception):
    """
    400 Bad Request
    """


class Forbidden(Exception):
    """
    403 Forbidden
    """


class ResourceNotFound(Exception):
    """
    404 Resource not found
    """


class ResourceGone(Exception):
    """
    410 Resource is no longer available
    """


class InternalServerError(Exception):
    """
    500 Internal Server Error
    """


class ConfigError(Exception):
    """
    Configuration not provided in api_map
    """
