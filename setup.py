# -*- coding: utf-8 -*-
#
# RERO ID
# Copyright (C) 2020 RERO.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

"""Identity server for the RERO services."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('rero_id', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='rero-id',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='rero-id Invenio',
    license='MIT',
    author='RERO',
    author_email='software@rero.ch',
    url='https://id.rero.ch',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'rero-id = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
        ],
        'invenio_base.blueprints': [
            'rero_id = rero_id.theme.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'rero_id_theme = rero_id.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'rero_id = rero_id.config',
        ],
        'invenio_i18n.translations': [
            'messages = rero_id',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
