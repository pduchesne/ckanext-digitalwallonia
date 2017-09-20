'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.plugins as p
from ckanext.spatial.interfaces import ISpatialHarvester
from ckan.common import json


class ADNThemePlugin(plugins.SingletonPlugin):
    '''ADN theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
    pass

class MetawalHarvester(p.SingletonPlugin):
    p.implements(ISpatialHarvester, inherit=True)

    def get_package_dict(self, context, data_dict):
        package_dict = data_dict['package_dict']
        json_config = data_dict['harvest_object'].source.config

        if json_config:
            config = json.loads(json_config)
            if ('license_id' not in package_dict and 'default_license_id' in config):
                package_dict['license_id'] = config['default_license_id']
        # check default license in harvest source config

        return package_dict