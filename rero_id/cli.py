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

"""CLI commands."""

import click
from flask import current_app
from flask.cli import with_appcontext
from invenio_db import db
from invenio_oauth2server.models import Client
from werkzeug.local import LocalProxy

_datastore = LocalProxy(lambda: current_app.extensions['security'].datastore)


@click.group()
def apps():
    """OAuth2 server application commands."""


@apps.command('create')
@click.argument('email')
@click.argument('name')
@click.argument('website_url')
@click.option('-r', 'redirect_uris', required=True, multiple=True)
@click.option('-d', '--description')
@click.option('-p', '--public/--no-public', default=False)
@click.option('-i', '--client-id', default='')
@click.option('-s', '--client-secret', default='')
@with_appcontext
def apps_create(email, name, website_url, redirect_uris, client_id,
                client_secret, description, public):
    """Create or update an OAuth2 application configuration."""
    user_obj = _datastore.get_user(email)
    if user_obj is None:
        raise click.UsageError('ERROR: User not found.')
    user_id = user_obj.get_id()
    # find existing configuration
    c = Client.query.filter_by(name=name).filter_by(user_id=user_id).first()
    if c:
        click.secho(
            'Found existing configuration. Will update the record.',
            fg='yellow')
    else:
        c = Client()
    # update parameters
    c.user_id = user_obj.get_id()
    c.name = name
    c.website = website_url
    c.description = description or ''
    c.is_confidential = not public
    c._redirect_uris = '\n'.join(redirect_uris)

    # check if client id is given else generate a new one
    if client_id:
        c.client_id = client_id
    else:
        c.reset_client_id()

    # check if client secret is given else generate a new one
    if client_secret:
        c.client_secret = client_secret
    else:
        c.reset_client_secret()
    db.session.add(c)
    db.session.commit()
    click.secho(
        'Oauth application: {name} has been pushed for: {email}'.format(
            name=name, email=email), fg='green')
