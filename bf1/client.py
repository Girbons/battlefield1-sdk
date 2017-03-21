import requests

from .exceptions import InvalidAPIKey, BadRequest, Forbidden, ResourceNotFound, \
    ResourceGone, InternalServerError


class BFAPI:
    def __init__(self, **kwargs):
        self.token = kwargs['token']
        self.platform = kwargs['platform']
        self.username = kwargs['username']
        self._session = requests.Session()
        self._header = {'TRN-Api-Key': self.token}

    def _evaluate_response(self, response):
        if response.status_code == 400:
            raise BadRequest
        elif response.status_code == 401:
            raise InvalidAPIKey
        elif response.status_code == 403:
            raise Forbidden


    def get_basic_stats(self):
        api_request = 'GEThttps://battlefieldtracker.com/bf1/api/Stats/BasicStats?platform={}&displayName={}'.format(self.platform, self.username)
        response = self._session.get(api_request, headers=self._header)
