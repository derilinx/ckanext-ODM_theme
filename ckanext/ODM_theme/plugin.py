import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from . import helpers as hlp


class Odm_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ODM_theme')

    def get_helpers(self):
        return {
            'get_odm_navigation': hlp.get_odm_navigation,
        }
