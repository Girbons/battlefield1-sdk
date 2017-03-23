=====================
Battlefield 1 Web API
=====================

Setup
=====

Coming soon on PyPI

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
    # vehicles call coming soon
    # weapon call coming soon

    # LOADOUT SERVICE
    bf.loadout_service.get_items()
    bf.loadout_service.get_items_gates()
    bf.loadout_service.get_kits()
    bf1.loadout_service.get_presets()
    bf1.loadout_service.get_equipped_dog_tags()

    # response format is in JSON
