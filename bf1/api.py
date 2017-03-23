from requests import request

from .api_map import _API_MAP

from .exceptions import InvalidAPIKey, BadRequest, Forbidden, ResourceNotFound, \
    ResourceGone, InternalServerError, Redirection


class Api:
    def __init__(self):
        self.base_endpoint = _API_MAP['current']['api_root']

    def request(self, url, api_key, method, **kwargs):
        complete_url = '{}{}'.format(self.base_endpoint, url)
        header = {'TRN-Api-Key': api_key}
        response = request(method=method, url=complete_url, headers=header)
        return self.handle_response(response)

    def handle_response(self, response):
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
