
class BadRequest(Exception):
    """
    400 Bad Request
    """


class ResourceNotFound(Exception):
    """
    404 Resource not found
    """


class ConfigError(Exception):
    """
    Configuration not provided in api_map
    """


class PlatformError(Exception):
    """
    Platform Error
    """


class EnvVarNotSet(Exception):
    """
    Environment variable is not set
    """
