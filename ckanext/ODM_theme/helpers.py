import json
from ckan.lib.helpers import helper_functions

import logging
log = logging.getLogger(__name__)

import os

def get_odm_navigation():

    filename = os.path.join(os.path.dirname(__file__), 'public', 'odm_nav_items.json')
    with open(filename) as f:
        menu_items = json.load(f)

    return helper_functions.get('nav_html_parsing')(menu_items)



