from . import api_map

from .resolvers import Resolver

default_api_map = api_map._API_MAP['current']['api']


class Battlefield:
    def __init__(self, api_map=None, **kwargs):
        self.api_map = api_map

    def __getattr__(self, name):
        instance = Battlefield(api_map=self.api_map[name])
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        resolver = Resolver()
        return resolver.resolve(api_map=self.api_map, **kwargs)


bf = Battlefield(api_map=default_api_map)
