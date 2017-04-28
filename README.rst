=================
Battlefield 1 SDK
=================
.. image:: https://badge.fury.io/py/battlefield1-sdk.svg
    :target: https://badge.fury.io/py/battlefield1-sdk
.. image:: https://travis-ci.org/Girbons/battlefield1-sdk.svg?branch=master
    :target: https://travis-ci.org/Girbons/battlefield1-sdk
.. image:: https://coveralls.io/repos/github/Girbons/battlefield1-sdk/badge.svg?branch=master
    :target: https://coveralls.io/github/Girbons/battlefield1-sdk?branch=master
.. image:: https://requires.io/github/Girbons/battlefield1-sdk/requirements.svg?branch=master
     :target: https://requires.io/github/Girbons/battlefield1-sdk/requirements/?branch=master
     :alt: Requirements Status

Setup
=====

From the command line::

    pip install battlefield1-sdk

Usage
======

GET API_KEY: request it here: https://battlefieldtracker.com/site-api/create

Examples
========

.. code-block:: python

    from bf1.battlefield import Battlefield
    # PLATFORM AVAILABLES
    # 'Xbox'
    # 'Playstation'
    # 'Pc'
    bf = Battlefield(username='YOUR USERNAME', api_key='YOUR API KEY', platform='YOUR PLATFORM')

    # STATS SERVICE
    bf.stats_service.basic_stats()
    bf.stats_service.detailed_stats()
    bf.stats_service.career_for_owned_games()

    # PROGRESSION SERVICE
    bf.progression_service.get_codex()
    bf.progression_service.get_dog_tags()
    bf.progression_service.get_filtered_codex()
    bf.progression_service.get_kit_ranks_map()
    bf.progression_service.get_medals()
    bf.progression_service.get_vehicle(vehicle='mark v landship')
    bf.progression_service.get_vehicles()
    bf.progression_service.get_weapon(weapon='c93')
    bf.progression_service.get_weapons()

    # LOADOUT SERVICE
    bf.loadout_service.get_items()
    bf.loadout_service.get_items_gates()
    bf.loadout_service.get_kits()
    bf.loadout_service.get_presets()
    bf.loadout_service.get_equipped_dog_tags()

    # response format is in JSON

Run Tests
=========

Export your API_KEY::

    export API_KEY='YOUR API KEY'

Run tox::

    tox
