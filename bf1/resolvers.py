from .api import Api
from .config.vehicles import VEHICLES
from .config.weapons import WEAPONS
from .exceptions import VehicleNotFound, WeaponNotFound


class Resolver:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.api = Api()

    def setup(self, username, platform, api_map=None, **kwargs):
        """
        Prepare the request with the correct url and method
        substitute the `{username}` and `{platform}` with
        the correct parameters
        """
        url = api_map['url']
        method = api_map['method']

        if 'platform' in url:
            url = url.replace('{platform}', 'platform={}'.format(platform))
        if 'username' in url:
            url = url.replace('{username}', 'displayName={}'.format(username))
        if '{vehicle} in url' and 'vehicle' in kwargs:
            url = url.replace('{vehicle}', 'vehicleId={}'.format(resolve_vehicle(kwargs['vehicle'])))
        if '{weapon}'in url and 'weapon' in kwargs:
            url = url.replace('{weapon}', 'weaponId={}'.format(resolve_weapon(kwargs['weapon'])))

        self.method = method
        self.url = url

    def resolve(self, username, api_key, platform, api_map=None, **kwargs):
        """
        Make the request
        """
        self.setup(username, platform, api_map=api_map, **kwargs)
        return self.api.request(url=self.url, method=self.method, api_key=api_key)


def resolve_vehicle(vehicle_name):
    try:
        return VEHICLES[vehicle_name]
    except KeyError:
        raise VehicleNotFound('Vehicle not found in configuration file')


def resolve_weapon(weapon_name):
    try:
        return WEAPONS[weapon_name]
    except KeyError:
        raise WeaponNotFound('Weapon not found in configuration file')
