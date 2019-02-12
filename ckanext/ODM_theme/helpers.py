import json
import logging
from ckanext.odm_nav.lib import odm_nav_helper as hlp
log = logging.getLogger(__name__)


def get_odm_navigation():

    filename = '/usr/lib/ckan-extensions/ckanext-ODM_theme/ckanext/ODM_theme/public/odm_nav_items.json'
    with open(filename) as file:
        menu_items = json.load(file)
    file.close()

    return hlp.nav_html_parsing(menu_items)



