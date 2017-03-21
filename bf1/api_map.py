_API_MAP = {
    'api_root': {
        'base_url': 'https://battlefieldtracker.com/bf1/api',

            'stats': {
                'api_request': 'Stats/',
                'api': {
                    'carreer_for_owned_games': {
                        'url': 'CareerForOwnedGames/',
                        'method': 'get',
                    },

                'basic_stats': {
                    'url': 'BasicStats/',
                    'method': 'get',
                    'description': 'Get user base stats'
                },

                'detailed_stats': {
                    'url': 'DetailedStats/',
                    'method': 'get',
                    'description': 'Get user detailed stats'
                },
            },

            'progression_service': {
                'api_request': 'Progression/',
                'api': {
                    'get_codex': {
                        'url': 'GetCodex',
                        'method': 'get'
                    },

                    'get_dog_tags': {
                        'url': 'GetDogTags',
                        'method': 'get'
                    },

                    'get_filtered_codex': {
                        'url': 'GetFilteredCodex',
                        'method': 'get'
                    },

                    'get_kit_ranks_map': {
                        'url': 'GetKitRanksMap',
                        'method': 'get'
                    },

                    'get_medals': {
                        'url': 'GetMedals',
                        'method': 'get'
                    },

                    'get_vehicle': {
                        'url': 'GetVehicle',
                        'method': 'get'
                    },

                    'get_vehicles': {
                        'url': 'GetVehicles',
                        'method': 'get'
                    },

                    'get_weapon': {
                        'url': 'GetWeapon',
                        'method': 'get'
                    },

                    'get_weapons': {
                        'url': 'GetWeapons',
                        'method': 'get'
                    },
                },
            },

            'loadout_service': {
                'api_request': 'Loadout/',
                'api': {

                    'get_items': {
                        'url': 'GetItems',
                        'method': 'get'
                    },

                    'get_item_gates': {
                        'url': 'GetItemGates',
                        'method': 'get'
                    },

                    'get_kits': {
                        'url': 'GetKits',
                        'method': 'get'
                    },

                    'get_presets': {
                        'url': 'GetPresets',
                        'method': 'get'
                    },

                    'get_equipped_dog_tags': {
                        'url': 'GetEquippedDogtags',
                        'method': 'get'
                    },
                }
            }
        }
    }
}
