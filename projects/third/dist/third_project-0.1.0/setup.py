# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libs.hello.world', 'third']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'third-project',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'David Vujic',
    'author_email': 'david@vujic.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
