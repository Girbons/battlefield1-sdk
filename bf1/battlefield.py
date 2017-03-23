from . import api_map

from .resolvers import Resolver


default_api_map = api_map._API_MAP['current']['api']


class Battlefield:
    def __init__(self, username, api_key, platform, api_map=None, **kwargs):
        self.username = username
        self.api_key = api_key
        self.platform = platform
        if api_map:
            self.api_map = api_map
        else:
            self.api_map = default_api_map

    def get_platform(self):
        if isinstance(self.platform, int):
            return self.platform
        elif 'Xbox' in self.platform:
            return 1
        elif 'Playstation' in self.platform:
            return 2
        elif 'Pc' in self.platform:
            return 3

    def __getattr__(self, name):
        instance = Battlefield(self.username, self.api_key, self.get_platform(), api_map=self.api_map[name])
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        resolver = Resolver()
        platform = self.get_platform()
        return resolver.resolve(self.username, self.api_key, platform, api_map=self.api_map, **kwargs)
