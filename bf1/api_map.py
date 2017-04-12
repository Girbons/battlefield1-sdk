_API_MAP = {
    'current': {
        'api_root': 'https://battlefieldtracker.com/bf1/api/',
        'api': {

            'stats_service': {
                'career_for_owned_games': {
                    'url': 'Stats/CareerForOwnedGames?{platform}&{username}',
                    'method': 'get'
                },

                'basic_stats': {
                    'url': 'Stats/BasicStats?{platform}&{username}',
                    'method': 'get'
                },

                'detailed_stats': {
                    'url': 'Stats/DetailedStats?{platform}&{username}',
                    'method': 'get'
                },

            },

            'progression_service': {
                'get_codex': {
                    'url': 'Progression/GetCodex?{platform}',
                    'method': 'get'
                },

                'get_dog_tags': {
                    'url': 'Progression/GetDogtags?{platform}&{username}',
                    'method': 'get'
                },

                'get_filtered_codex': {
                    'url': 'Progression/GetFilteredCodex?{platform}&{username}',
                    'method': 'get'
                },

                'get_kit_ranks_map': {
                    'url': 'Progression/GetKitRanksMap?{platform}&{username}',
                    'method': 'get'
                },

                'get_medals': {
                    'url': 'Progression/GetMedals?{platform}&{username}',
                    'method': 'get'
                },

                'get_vehicle': {
                    'url': 'Progression/GetVehicle?{platform}&{username}&{vehicle}',
                    'method': 'get'
                },

                'get_vehicles': {
                    'url': 'Progression/GetVehicles?{platform}&{username}',
                    'method': 'get'
                },

                'get_weapon': {
                    'url': 'Progression/GetWeapon?{platform}&{username}&{weapon}',
                    'method': 'get'
                },

                'get_weapons': {
                    'url': 'Progression/GetWeapons?{platform}&{username}',
                    'method': 'get'
                },
            },

            'loadout_service': {
                'get_items': {
                    'url': 'Loadout/GetItems?{platform}',
                    'method': 'get'
                },

                'get_items_gates': {
                    'url': 'Loadout/GetItemGates?{platform}',
                    'method': 'get'
                },

                'get_kits': {
                    'url': 'Loadout/GetKits?{platform}',
                    'method': 'get'
                },

                'get_presets': {
                    'url': 'Loadout/GetPresets?{platform}&{username}',
                    'method': 'get'
                },

                'get_equipped_dog_tags': {
                    'url': 'Loadout/GetEquippedDogtags?{platform}&{username}',
                    'method': 'get'
                },
            }
        }
    }
}
