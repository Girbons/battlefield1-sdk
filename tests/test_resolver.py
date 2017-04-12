import pytest

from bf1.resolvers import resolve_weapon, resolve_vehicle
from bf1.exceptions import WeaponNotFound, VehicleNotFound


def test_weapon_solver():
    weapon_name = 'lewis gun low weight'
    weapon_id = resolve_weapon(weapon_name)
    assert weapon_id == 'b79b965e-e080-475d-a1cc-2432de5f3bf5'


def test_weapon_solver_error():
    with pytest.raises(WeaponNotFound) as ex_info:
        resolve_weapon('test-weapon')
    assert 'Weapon not found in configuration file' in str(ex_info.value)


def test_vehicle_solver():
    vehicle_name = 'mark v landship'
    vehicle_id = resolve_vehicle(vehicle_name)
    assert vehicle_id == '4723a26f-98ae-55ba-7b3f-3ae7e0e3b0c7'


def test_vehicle_solver_error():
    with pytest.raises(VehicleNotFound) as ex_info:
        resolve_vehicle('test-vehicle')
    assert 'Vehicle not found in configuration file' in str(ex_info.value)
