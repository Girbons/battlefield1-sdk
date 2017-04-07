from . import api_map

from .exceptions import ConfigError, PlatformError
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
        """
        For each platform is associated an integer
        1: xbox
        2: playstation
        3: pc
        """
        if isinstance(self.platform, int):
            return self.platform
        elif 'Xbox' in self.platform:
            return 1
        elif 'Playstation' in self.platform:
            return 2
        elif 'Pc' in self.platform:
            return 3
        else:
            raise PlatformError('Platform unavailable')

    def __getattr__(self, name):
        """
        Return a battlefield instance
        """
        if name not in self.api_map:
            raise ConfigError('Configuration not available in api_map for this call')
        instance = Battlefield(self.username, self.api_key, self.get_platform(), api_map=self.api_map[name])
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        """
        The request happens here
        return JSON response
        """
        resolver = Resolver()
        platform = self.get_platform()
        return resolver.resolve(self.username, self.api_key, platform, api_map=self.api_map, **kwargs)
