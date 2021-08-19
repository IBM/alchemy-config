#*****************************************************************#
# (C) Copyright IBM Corporation 2020.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
#*****************************************************************#
'''Holds all common fixtures used in unit tests.
'''

import os


# Common fixtures ##################################################################################

GOOD_FLAT_DICT = {
    'none_key': None,
    'int_key': 1,
    'str_key': 'string',
    'float_key': 3.14,
    'list_key': [
        0, 1, 2, 3,
    ],
}

GOOD_NESTED_DICT = {
    'key1': {
        'key3': {
            'none_key': None,
            'int_key': 1,
        },
    },
    'key2': {
        'key4': {
            'key5': {
                'str_key': 'string',
            },
            'float_key': 3.14,
        },
    },
    'list_key': [
        0, 1, 2, 3,
    ],
}

NOT_YAML_CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), "nonexistent_config")
BAD_CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), "nonexistent_config.yaml")
METHOD_NAME_CONFLICT_CONFIG_LOCATION = os.path.join(
    os.path.dirname(__file__), "method_name_conflict.yaml")
GOOD_CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), "good_config.yaml")
