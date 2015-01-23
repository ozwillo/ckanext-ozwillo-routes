from pylons import config

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class OzwilloRoutesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)

    def before_map(self, map):
        # parameter defined in deployment config file
        # for example user_profile_edit_url = https://portal.oasis-eu.org/my/profile
        user_profile_url = config.get('ckanext.ozwillo_routes.user_profile_edit_url', '/')
        map.redirect('/user/edit', user_profile_url)
        map.redirect('/user/edit/{id:.*}', user_profile_url)
        map.redirect('/user/reset', user_profile_url)
        return map

    def after_map(self, map):
        return map
