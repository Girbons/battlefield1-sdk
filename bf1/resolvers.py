from .api import Api


class Resolver:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.api = Api()

    def setup(self, username, platform, api_map=None, **kwargs):
        url = api_map['url']
        method = api_map['method']

        if 'platform' in url:
            url = url.replace('{platform}', 'platform={}'.format(platform))
        if 'username' in url:
            url = url.replace('{username}', 'displayName={}'.format(username))

        self.method = method
        self.url = url

    def resolve(self, username, api_key, platform, api_map=None, **kwargs):
        self.setup(username, platform, api_map=api_map, **kwargs)
        return self.api.request(url=self.url, method=self.method, api_key=api_key)
