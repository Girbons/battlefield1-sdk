import os

from bf1.exceptions import EnvVarNotSet


def get_token():
    try:
        return os.environ['API_KEY']
    except KeyError:
        raise EnvVarNotSet('API_KEY')


API_KEY = get_token()
METHOD = 'get'
