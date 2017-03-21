from requests import request

from .exceptions import InvalidAPIKey, BadRequest, Forbidden, ResourceNotFound, \
    ResourceGone, InternalServerError, Redirection


class BfApi:
    def __init__(self, **kwargs):
        self.api_key = kwargs['token']
        self.platform = kwargs['platform']
        self.username = kwargs['username']
        self._header = {'TRN-Api-Key': self.api_key}

    def _evaluate_response(self, response):
        status_code = response.status_code
        if status_code in (301, 302, 303, 307):
            raise Redirection
        elif 200 <= status_code <= 299:
            return response.json()
        elif status_code == 400:
            raise BadRequest
        elif status_code == 401:
            raise InvalidAPIKey
        elif status_code == 403:
            raise Forbidden
        elif status_code == 404:
            raise ResourceNotFound
        elif status_code == 410:
            raise ResourceGone
        elif status_code == 500:
            raise InternalServerError

