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
        raise_exception = False

        if isinstance(self.platform, int) and self.platform >= 1 and self.platform <= 3:
            return self.platform
        try:
            if 'xbox' in self.platform.lower():
                return 1
            elif 'playstation' in self.platform.lower():
                return 2
            elif 'pc' in self.platform.lower():
                return 3
            else:
                raise_exception = True
        except:
            raise_exception = True

        if raise_exception:
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
