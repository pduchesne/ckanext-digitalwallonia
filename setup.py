from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-digitalwallonia',
    version=version,
    description="Agence du Numerique",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Agence du Numerique (Quentin Meulepas)',
    author_email='quentin.meulepas@adn.be',
    url='http://www.adn.be',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.digitalwallonia'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
	digitalwallonia_theme=ckanext.digitalwallonia.plugin:ADNThemePlugin
    ''',
)
