from .api import Api


class Resolver:
    def __init__(self):
        self.platform = 1
        self.username = 'girbons'
        self.url = ''
        self.method = ''
        self.api = Api()

    def setup(self, api_map=None, **kwargs):
        url = api_map['url']
        method = api_map['method']

        if 'platform' in url:
            url = url.replace('{platform}', 'platform={}'.format(self.platform))
        if 'username' in url:
            url = url.replace('{username}', 'displayName={}'.format(self.username))

        self.method = method
        self.url = url

    def resolve(self, api_map=None, **kwargs):
        self.setup(api_map=api_map, **kwargs)
        return self.api.request(url=self.url)
