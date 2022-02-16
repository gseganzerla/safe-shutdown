# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['safe_shutdown', 'safe_shutdown.models', 'safe_shutdown.services']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.0,<6.0.0']

entry_points = \
{'console_scripts': ['safe-shutdown = safe_shutdown:__main__']}

setup_kwargs = {
    'name': 'safe-shutdown',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Guilherme Seganzerla',
    'author_email': 'g.seganzerla@gmail.com',
    'maintainer': 'gseganzerla',
    'maintainer_email': 'g.seganzerla@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

