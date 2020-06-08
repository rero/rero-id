#!/usr/bin/env bash
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


pipenv check && \
pipenv run pydocstyle rero_id tests docs && \
pipenv run isort -rc -c -df && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
