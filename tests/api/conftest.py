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

"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

import tempfile

import pytest
from invenio_app.factory import create_api


@pytest.fixture(scope='module')
def app_config(app_config):
    """Get app config."""
    app_config['CELERY_ALWAYS_EAGER'] = True
    return app_config


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api
